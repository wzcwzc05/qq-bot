import plugins.ClassMain
import requests

class test(plugins.ClassMain.MessageEvent):             #从plugins.ClassMain.MessageEvent继承
    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid, gid=None) -> None:
        super().__init__(Http_Port, IsGroup, IsPrivate, Message, uid, gid)

    def MessageDeal(self):                              #重写方法
        address = "http://127.0.0.1:" + str(self.Http)
        if (self.gid == None):
            requests.get(
                url=address + '/send_private_msg?user_id={0}&message={1}'.format(self.uid, "Hello,World!"))
        elif (self.gid != None):
            requests.get(
                url=address + '/send_group_msg?group_id={0}&message={1}'.format(self.gid, "Hello,World!"))
