from flask import Flask, request, abort
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from getGood import Web
from lineAPI import LineAPI
import json
import sqlite3
#from createDB import MyDB
#conn = MyDB()
loveTable = "love"
videoTable = "newVideo"



app = Flask(__name__)
with open("config.json") as file:
    config = json.load(file)
line_bot_api = LineBotApi(config["access_token"])
handler = WebhookHandler(config["channel"])
my_api = LineAPI(config["access_token"])
webs = {}



#print(my_api.getHeader())
#create rich menu
#req = requests.request('POST', my_api.createRichMenuURL() ,headers=my_api.getHeader(), data=json.dumps(my_api.getRichBody()).encode('utf-8'))
# upload rich menu image
"""with open("image/menu.jpg",'rb') as f:
    line_bot_api.set_rich_menu_image(my_api.getRichMenuID(), "image/jpeg",f)"""
#post rich menu

req = requests.request('POST', my_api.getRichMenuURL(),headers=my_api.getHeader())
rich_menu_list = line_bot_api.get_rich_menu_list()
from threading import Thread
from time import sleep
id = config["userID"]
def call_at_interval(period, callback, args):
    while True:
        sleep(period)
        callback(*args)

def setInterval(period, callback, *args):
    return Thread(target=call_at_interval, args=(period, callback, args))

def hello(word):
    print("hello", word)


#t = setInterval(60,updateNew)
#t.start()

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print(event)
    if not existID(event.source.user_id):
        with sqlite3.connect('userLove.db') as conn:
            c = conn.cursor()
            c.executemany('INSERT INTO userTable(userID, Ga, Tsai, How, office, hot, Geography) VALUES (?,?,?,?,?,?,?)', [(event.source.user_id,1,1,1,1,1,1)])
            conn.commit()
    if event.message.text == 'get':
        message = getMylove(webs[0])
    elif event.message.text == 'choose':
        message = choose()
    elif event.message.text in urls:
        message = getMylove(webs[event.message.text])

    else :
        message = TextSendMessage(text=event.message.text)

    line_bot_api.reply_message(event.reply_token, message)


def getMylove(web):
    href = web.get_Newest()

    return TextSendMessage(text=href)
def choose():
    pass
def existID(id):
    with sqlite3.connect('userLove.db') as conn:
        c = conn.cursor()

        for row in c.execute('SELECT * FROM userTable where userID="'+id+'"'):
            return True
        return False

with open("url.json") as file:
    urls = json.load(file)
    for url in urls:
        webs[url] = Web(url,urls[url],line_bot_api)

print(webs)

import os
if __name__ == "__main__":

    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
