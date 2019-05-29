from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/Users/tarasziniak/PycharmProjects/Parserv2/index.html"), "html.parser")
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='taras193', passwd='123qwe332', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

listartist = soup.findAll('a',{'class':'artist_link'})
for child in listartist:
    print (child.contents)
print(listartist)

# listsongs = soup.findAll('span',{'class':'audio_row__title_inner _audio_row__title_inner'})
# for child in listsongs:
#     print (child.contents)
# print(listsongs)

# listduration = soup.findAll('div',{'class':'audio_row__duration audio_row__duration-s _audio_row__duration'})
# for child in listduration:
#     print (child.contents)
# print(listduration)



try:

    with cur as cursor:
        for x in listartist:
            sqlQuerry = "INSERT INTO playlist (ARTIST) VALUES (\"%s\")"
            cursor.execute(sqlQuerry, (x))
            conn.commit()
except pymysql.OperationalError: print('Unknown base name')
finally:
    cur.close()
    conn.close()
