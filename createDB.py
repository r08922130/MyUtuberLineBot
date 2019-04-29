import sqlite3



conn = sqlite3.connect('userLove.db')
c = conn.cursor()
c.execute('''CREATE TABLE newVideo
             (ID INTEGER PRIMARY KEY,
              name NOT NULL,
              url NOT NULL)''')
c.executemany('INSERT INTO newVideo(name, url) VALUES (?,?)', [('Tsai','hello')])
conn.commit()
for row in c.execute('SELECT * FROM newVideo where name="Tsai"'):
    print(row)
conn.close()
