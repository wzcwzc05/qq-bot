from plugins import *


class test(ClassMain.MessageEvent):
    def __init__(self, Http_Port, IsGroup, IsPrivate, Message, uid) -> None:
        super().__init__(Http_Port, IsGroup, IsPrivate, Message, uid)

    def MessageDeal(self):
        return super().MessageDeal()
