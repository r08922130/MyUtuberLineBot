from linebot import (
    LineBotApi, WebhookHandler
)
line_bot_api = LineBotApi(config["access_token"])
rich_menu_list = line_bot_api.get_rich_menu_list()
for rich_menu in rich_menu_list:
    line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
try:
    os.remove("menuID.json")
except:
    print("Error while deleting file ", "menuID.json")
