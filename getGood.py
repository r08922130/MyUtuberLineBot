import requests
import sqlite3
import time
import threading
from bs4 import BeautifulSoup
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
class Web(threading.Thread):
    def __init__(self,name,url,lineBot=None):
        threading.Thread.__init__(self)
        self.name = name
        self.url = url
        #kill thread when main thread is killed
        self.daemon = True
        self.lineBot = lineBot
        self.start()
    def run(self):
        while True:
            self.searchNewest(auto=True)
            time.sleep(60)
    def get_Newest(self):
        #select from DB
        with sqlite3.connect('userLove.db') as conn:
            c = conn.cursor()
            #print(self.name)

            for row in self.newest(c):
                print(row)
                return row[0]

            self.createNewLabel()
            return self.searchNewest()
    def newest(self,c):
        return c.execute('SELECT url FROM newVideo where name="'+self.name+'"')
    def createNewLabel(self):
        with sqlite3.connect('userLove.db') as conn:
            c = conn.cursor()
            c.executemany('INSERT INTO newVideo(name, url) VALUES (?,?)', [(self.name,self.url)])
            conn.commit()
    def searchNewest(self,auto=False):
        request = requests.get(self.url)
        content = request.content
        soup=BeautifulSoup(content,"html.parser")
        container = soup.select("h3 a")
        #print(container[0].get_text(),container[0]['href'])
        if len(container)>0:
            href = "www.youtube.com"+container[0]['href']

            with sqlite3.connect('userLove.db') as conn:

                c = conn.cursor()
                if self.lineBot:
                    for row in self.newest(c):
                        #update DB
                        if row[0] != href:
                            print(row)
                            if auto:
                                for id in c.execute('SELECT userID FROM '+self.name+'Table where like='+str(1)):
                                    #print(row[0])
                                    self.lineBot.push_message(id[0],TextSendMessage(text=href))

                            c.execute('UPDATE newVideo SET url = ? WHERE name = ?',(href, self.name))
                            conn.commit()
        else:
            href = self.searchNewest(auto=auto)


        return href
