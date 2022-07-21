import requests
from plugins import api


class MessageEvent():               # 消息事件类
    IsGroup = False                 # 消息是否来自群组
    IsPrivate = False               # 消息是否来自私人
    Message = ""                    # 消息内容
    uid = ""                        # 消息发送者uid
    gid = None                      # 消息发送群组的gid    

    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid, gid=None) -> None:
        self.Http = Http_Port
        self.IsGroup = IsGroup
        self.IsPrivate = IsPrivate
        self.Message = Message
        self.uid = uid
        self.gid = gid

    def MessageDeal(self):          # 消息处理函数
        raise NotImplementedError("Not implemented!")
