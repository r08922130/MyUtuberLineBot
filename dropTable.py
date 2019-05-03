import sqlite3



conn = sqlite3.connect('userLove.db')
c = conn.cursor()
c.execute('DROP TABLE userTable')
#c.executemany('INSERT INTO newVideo(name, url) VALUES (?,?)', [('Tsai','hello')])
#conn.commit()
for row in c.execute('SELECT * FROM newVideo where name="Tsai"'):
    print(row)
conn.close()
