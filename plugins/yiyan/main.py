import plugins.ClassMain
import requests
import json


class yiyan(plugins.ClassMain.MessageEvent):
    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid, gid=None) -> None:
        super().__init__(Http_Port, IsGroup, IsPrivate, Message, uid, gid)

    def MessageDeal(self):
        address = "http://127.0.0.1:" + str(self.Http)
        Joke = requests.get(
            "https://api.muxiaoguo.cn/api/yiyan?api_key=4ef64f29d4dd13fb")
        message = json.loads(Joke.text)["data"]["content"]
        if (json.loads(Joke.text)["data"]["derivation"]!=None):
            author = "——————" + json.loads(Joke.text)["data"]["derivation"]
        else:
            author = ""
        if (self.gid == None):
            self.SendPrivateMessage(self.uid, message + author)
        elif (self.gid != None):
            self.SendGroupMessage(self.gid, message + author)
