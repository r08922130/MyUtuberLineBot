import requests
import sqlite3
from bs4 import BeautifulSoup
class Web():
    def __init__(self,name,url):
        self.name = name
        self.url = url
    def get_Newest(self,):
        #select from DB
        with sqlite3.connect('userLove.db') as conn:
            c = conn.cursor()
            print(self.name)

            for row in c.execute('SELECT * FROM newVideo where name="'+self.name+'"'):
                print(row)
                return self.searchNewest()


            return self.searchNewest()


    def searchNewest(self):
        request = requests.get(self.url)
        content = request.content
        soup=BeautifulSoup(content,"html.parser")
        container = soup.select("h3 a")
        #print(container[0].get_text(),container[0]['href'])
        href = "www.youtube.com"+container[0]['href']

        #update DB
        return container[0].get_text(),href
        """for item in container:
            value = item.get_text()
            print(value, item['href'])"""




#web = Web("https://www.youtube.com/user/coolmantsai/videos")
#web.get_Newest()

#print(content)

#file = open('result.text','w')
#file.write(soup.get_text() + '\n')

#print(container)
#
"""for item in container:
    value = item.get_text()
    print(value)
    file.write(value + '\n')"""
#file.close()
