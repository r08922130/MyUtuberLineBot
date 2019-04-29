class LineAPI():
    def __init__(self,access_token):

        self.access_token = access_token
    def createRichMenuURL(self):
        return 'https://api.line.me/v2/bot/richmenu'
    def getRichMenuURL(self):
        return 'https://api.line.me/v2/bot/user/all/richmenu/'+self.getRichMenuID()
    def getHeader(self):
        return {"Authorization":"Bearer "+self.access_token,"Content-Type":"application/json"}

    def getRichBody(self):
        return {
            "size":{"width":2500, "height":1686},
            "selected": "true",
            "name": "Controller",
            "chatBarText":"Controller",
            "areas":[
                {
                    "bounds":{"x":25, "y":18, "width":800,"height":816},
                    "action":{"type":"message", "text":"up"}
                },{
                    "bounds":{"x":850, "y":18, "width":800,"height":816},
                    "action":{"type":"message", "text":"right"}
                },{
                    "bounds":{"x":1675, "y":18, "width":800,"height":816},
                    "action":{"type":"message", "text":"down"}
                },{
                    "bounds":{"x":25, "y":852, "width":800,"height":816},
                    "action":{"type":"message", "text":"left"}
                },{
                    "bounds":{"x":850, "y":852, "width":800,"height":816},
                    "action":{"type":"message", "text":"btn b"}
                },{
                    "bounds":{"x":1675, "y":852, "width":800,"height":816},
                    "action":{"type":"message", "text":"btn a"}
                }
            ]

        }
    def getRichMenuID(self):
        return "richmenu-9ee7d4ef2513c181087711f4c4308e06"
