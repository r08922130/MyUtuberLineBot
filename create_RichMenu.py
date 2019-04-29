
import requests
import json
import os
from lineAPI import LineAPI
my_api = LineAPI(config["access_token"])
req = requests.request('POST', my_api.createRichMenuURL() ,headers=my_api.getHeader(), data=json.dumps(my_api.getRichBody()).encode('utf-8'))
print(req.text)
try:
    os.remove("menuID.json")
except:
    print("Error while deleting file ", "menuID.json")
with open("menuID.json","w+") as file:
    file.write('{"menuID":'+req.text+'}')
