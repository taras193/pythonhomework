from bs4 import BeautifulSoup
file = open('/Users/tarasziniak/PycharmProjects/Parserv2/index.html', 'r', encoding="ISO-8859-1");
soup = BeautifulSoup(file, "html.parser")
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='taras193', passwd='123qwe332', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

artist_add_sqlQuerry = "INSERT INTO playlist (ARTIST, SONG, DURATION) VALUES (\"%s\",\"%s\",\"%s\")"

listartist = soup.findAll('a',{'class':'artist_link'})
listsongs = soup.findAll('span',{'class':'audio_row__title_inner _audio_row__title_inner'})
listduration = soup.findAll('div',{'class':'audio_row__duration audio_row__duration-s _audio_row__duration'})

l = min(len(listartist), len(listsongs), len(listduration) );

for i in range (0,l):
    cur.execute(artist_add_sqlQuerry,[(listartist.pop().contents),(listsongs.pop().contents), (listduration.pop().contents)])

cur.connection.commit()
cur.close()






