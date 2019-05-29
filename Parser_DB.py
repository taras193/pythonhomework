#V1
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(open("/Users/tarasziniak/PycharmProjects/Parserv2/index.html"), "html.parser")
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='taras193', passwd='123qwe332', db='scraping', charset='utf8')
# cur = conn.cursor()
# cur.execute("USE scraping")
#
# artist_add_sqlQuerry = "INSERT INTO playlist (ARTIST) VALUES (\"%s\")"
# song_add_sqlQuerry = "INSERT INTO playlist (SONG) VALUES (\"%s\")"
# duration_add_sqlQuerry = "INSERT INTO playlist (DURATION) VALUES (\"%s\")"
#
#
# listartist = soup.findAll('a',{'class':'artist_link'})
# for child in listartist:
#     cur.execute(artist_add_sqlQuerry,(child.contents))
#     cur.connection.commit()
#
#
# listsongs = soup.findAll('span',{'class':'audio_row__title_inner _audio_row__title_inner'})
# for child in listsongs:
#     cur.execute(song_add_sqlQuerry,(child.contents))
#     cur.connection.commit()
#
# listduration = soup.findAll('div',{'class':'audio_row__duration audio_row__duration-s _audio_row__duration'})
# for child in listduration:
#     cur.execute(duration_add_sqlQuerry,(child.contents))
#     cur.connection.commit()
#
# cur.close()
# conn.close()
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/Users/tarasziniak/PycharmProjects/Parserv2/index.html"), "html.parser")
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='taras193', passwd='123qwe332', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

artist_add_sqlQuerry = "INSERT INTO playlist (ARTIST) VALUES (\"%s\")"
song_add_sqlQuerry = "INSERT INTO playlist (SONG) VALUES (\"%s\")"
duration_add_sqlQuerry = "INSERT INTO playlist (DURATION) VALUES (\"%s\")"


listartist = soup.findAll('a',{'class':'artist_link'})
listsongs = soup.findAll('span',{'class':'audio_row__title_inner _audio_row__title_inner'})
listduration = soup.findAll('div',{'class':'audio_row__duration audio_row__duration-s _audio_row__duration'})

for child in listartist:
    cur.execute(artist_add_sqlQuerry,(child.contents))

for child in listsongs:
    cur.execute(song_add_sqlQuerry,(child.contents))

for child in listduration:
    cur.execute(duration_add_sqlQuerry,(child.contents))

cur.connection.commit()
cur.close()
conn.close()