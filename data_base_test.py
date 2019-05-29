import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='taras193', passwd='123qwe332', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

a='testartist'
b='testsong'
try:
    with cur as cursor:
        sqlQuerry = "INSERT INTO playlist (ARTIST, SONG) VALUES (\"%s\", \"%s\")"
        cursor.execute(sqlQuerry, (a, b))
        conn.commit()
except pymysql.OperationalError: print('Unknown base name')
finally:
    cur.close()
    conn.close()