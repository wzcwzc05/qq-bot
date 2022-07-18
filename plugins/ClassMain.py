import requests
from plugins import api


class MessageEvent():
    IsGroup = False
    IsPrivate = False
    Message = ""
    uid = ""

    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid) -> None:
        self.Http = Http_Port
        self.IsGroup = IsGroup
        self.IsPrivate = IsPrivate
        self.Message = Message
        self.uid = uid

    def MessageDeal(self):
        raise NotImplementedError("Not implemented!")
