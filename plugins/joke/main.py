import plugins.ClassMain
import requests
import json

class joke(plugins.ClassMain.MessageEvent):
    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid, gid=None) -> None:
        super().__init__(Http_Port, IsGroup, IsPrivate, Message, uid, gid)

    def MessageDeal(self):
        address = "http://127.0.0.1:" + str(self.Http)
        Joke = requests.get(
            "https://api.muxiaoguo.cn/api/xiaohua?api_key=5c3c4cd312256538")
        message = json.loads(Joke.text)["data"]["content"]
        if (self.gid == None):
            requests.get(
                url=address + '/send_private_msg?user_id={0}&message={1}'.format(self.uid, message))
        elif (self.gid != None):
            requests.get(
                url=address + '/send_group_msg?group_id={0}&message={1}'.format(self.gid, message))

