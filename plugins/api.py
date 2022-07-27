import requests
import json
import time
from plugins import ClassMain
import plugins
import logging
import os


def enterance(http_port, message, uid, gid=None):       # 进入插件系统

    with open("./plugins/plugins.json", 'r') as load_f:
        PluginsData = json.load(load_f)
    PluginsList = PluginsData["plugins"]
    address = "http://127.0.0.1:" + str(http_port)
    
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("./logs/api.log", encoding="UTF-8")
    formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                 datefmt="%Y/%m/%d %X")
    fh.setFormatter(formator)

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

        # 如果是定时插件且插件处于激活状态（未开发完成）
        if (plugin["type"] == "schedule") and (plugin["active"] == True):
            pass
