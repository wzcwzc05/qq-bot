import requests
from plugins import api

class MessageEvent():
    IsGroup = False
    IsPrivate = False
    Message = ""
    uid = ""
    def __init__(self,IsGroup,IsPrivate,Message,uid) -> None:
        self.IsGroup=IsGroup
        self.IsPrivate=IsPrivate
        self.Message=Message
        self.uid=uid

      