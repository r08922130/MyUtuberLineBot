import sqlite3



conn = sqlite3.connect('userLove.db')
c = conn.cursor()
c.execute('''CREATE TABLE userTable
             (ID INTEGER PRIMARY KEY,
              userID INTEGER NOT NULL,
              Ga INTEGER NOT NULL,
              Tsai INTEGER NOT NULL,
              How INTEGER NOT NULL,
              office INTEGER NOT NULL,
              hot INTEGER NOT NULL,
              Geography INTEGER NOT NULL)''')
#c.executemany('INSERT INTO newVideo(name, url) VALUES (?,?)', [('Tsai','hello')])
#conn.commit()
for row in c.execute('SELECT * FROM newVideo where name="Tsai"'):
    print(row)
conn.close()
