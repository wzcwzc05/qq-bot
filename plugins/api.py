import requests
import json
import time
from plugins import ClassMain
import plugins


def enterance(http_port, message, uid, gid=None):

    with open("./plugins/plugins.json", 'r') as load_f:
        PluginsData = json.load(load_f)
    print(PluginsData)
    PluginsList = PluginsData["plugins"]
    address = "http://127.0.0.1:" + str(http_port)

    for plugin in PluginsList:
        if (plugin["type"] == "command") and (plugin["active"] == True):
            #__import__(plugin["name"])
            if (plugin["commands"]["IsGroup"] == False) and (gid != None):
                continue
            if (plugin["commands"]["IsPrivate"] == False) and (gid == None):
                continue
            if (plugin["commands"]["uid"]):
                flag = False
                for puid in plugin["uid"]:
                    if (puid == uid):
                        flag = True
                        break
                if (flag == False):
                    continue
            StrictMode = plugin["commands"]["strict"]
            entry = plugin["entry"]

            if (StrictMode == True):
                for word in plugin["commands"]["words"]:
                    if (message == word):
                        if (gid == None):
                            requests.get(
                                url=address + '/send_private_msg?user_id={0}&message={1}'.format(uid, "别叫了，我在"))
                        elif (gid != None):
                            requests.get(
                                url=address + '/send_group_msg?group_id={0}&message={1}'.format(gid, "别叫了，我在"))

            else:
                for word in plugin["commands"]["words"]:
                    if (message.find(word) != -1):
                        pass
        if (plugin["type"] == "schedule") and (plugin["active"] == True):
            pass