import json
import logging
import os
import plugins
import plugins.globalvar as gl


def enterance(http_port: int, message: str, uid: int, gid=None) -> None:       # 进入插件系统

    if gl.get_value("plugins_list") == None:
        with open("./plugins/plugins.json", 'r') as load_f:
            PluginsData = json.load(load_f)
        PluginsList = PluginsData["plugins"]
        gl.set_value("plugins_list", PluginsList)
    else:
        PluginsList = gl.get_value("plugins_list")
    address = "http://127.0.0.1:" + str(http_port)

    for plugin in PluginsList:
        if (plugin["type"] == "command") and (plugin["active"] == True):        # 如果是命令插件且插件处于激活状态
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
            # 获取是否严格匹配模式
            StrictMode = plugin["commands"]["strict"]

            if (StrictMode == True):
                for word in plugin["commands"]["words"]:
                    if (message == word):                                   # 如果严格匹配到了指定的指令
                        Exec = "plugins." + \
                            plugin["name"]+"."+plugin["entry"] + \
                            "."+plugin["name"]
                        if (gid == None):
                            Temp = eval(Exec)(
                                http_port, False, True, message, uid, gid)
                        else:
                            Temp = eval(Exec)(
                                http_port, True, False, message, uid, gid)
                        Temp.MessageDeal()
                        del Temp
            else:
                for word in plugin["commands"]["words"]:
                    if (message.find(word) != -1):                          # 如果匹配到了关键词
                        Exec = "plugins." + \
                            plugin["name"]+"."+plugin["entry"] + \
                            "."+plugin["name"]
                        if (gid == None):
                            Temp = eval(Exec)(
                                http_port, False, True, message, uid, gid)
                        else:
                            Temp = eval(Exec)(
                                http_port, True, False, message, uid, gid)
                        Temp.MessageDeal()
                        del Temp

        # 如果是定时插件且插件处于激活状态（未开发完成）
        if (plugin["type"] == "schedule") and (plugin["active"] == True):
            pass
