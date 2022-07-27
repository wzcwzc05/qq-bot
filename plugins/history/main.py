from calendar import month

from matplotlib.pyplot import title
import plugins.ClassMain
import requests
import json
import random

class history(plugins.ClassMain.MessageEvent):
    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid, gid=None) -> None:
        super().__init__(Http_Port, IsGroup, IsPrivate, Message, uid, gid)

    def MessageDeal(self):
        address = "http://127.0.0.1:" + str(self.Http)
        Joke = requests.get(
            "https://api.muxiaoguo.cn/api/lishijr?api_key=c7cbb62f2dfecf40")
        message = random.choice(json.loads(Joke.text)["data"])
        year = message["year"]
        month = message["month"]
        day = message["day"]
        title = message["title"]
        if (self.gid == None):
            self.SendPrivateMessage(self.uid, "历史上的今天是" + str(year) + "年" + str(month) + "月" + str(day) + "日，" + title)
        elif (self.gid != None):
            self.SendGroupMessage(self.gid, "历史上的今天是" + str(year) + "年" + str(month) + "月" + str(day) + "日，" + title)
