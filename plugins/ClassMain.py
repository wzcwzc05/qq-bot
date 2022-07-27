import requests
from plugins import api
import logging


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
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("./logs/api.log", encoding="UTF-8")
        formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                     datefmt="%Y/%m/%d %X")
        fh.setFormatter(formator)
        logger.addHandler(fh)
        logger.info(type(self).__name__ + ": " + "Init Successful!")

    def MessageDeal(self):          # 消息处理函数
        raise NotImplementedError("MessageDeal Not implemented!")

    def _logm(self):                                        # 日志输出函数
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("./logs/api.log", encoding="UTF-8")
        formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                     datefmt="%Y/%m/%d %X")
        fh.setFormatter(formator)
        logger.addHandler(fh)
        return logger

    def SendPrivateMessage(self, uid, message):                 # 发送私人消息
        address = "http://127.0.0.1:" + str(self.Http)
        try:
            requests.get(
                url=address + '/send_private_msg?user_id={0}&message={1}'.format(uid, message))
            self._logm().error(type(self).__name__ +
                               ": Send private message to {0} successfully!".format(uid))
        except requests.exceptions.ConnectionError:
            self._logm().error(type(self).__name__ + ": ---ConnectionError---")
        except requests.exceptions.Timeout:
            self._logm().error(type(self).__name__ + ": ---Timeout---")
        except requests.exceptions.ChunkedEncodingError:
            self._logm().error(type(self).__name__ + ": ---ChunkedEncodingError---")
        except:
            self._logm().error(type(self).__name__ + ": ---UnknownError---")

    def SendGroupMessage(self, gid, message):                   # 发送群组消息
        address = "http://127.0.0.1:" + str(self.Http)
        try:
            requests.get(
                url=address + '/send_group_msg?group_id={0}&message={1}'.format(gid, message))
            self._logm().error(type(self).__name__ +
                               ": Send group message to {0} successfully!".format(gid))
        except requests.exceptions.ConnectionError:
            self._logm().error(type(self).__name__ + ": ---ConnectionError---")
        except requests.exceptions.Timeout:
            self._logm().error(type(self).__name__ + ": ---Timeout---")
        except requests.exceptions.ChunkedEncodingError:
            self._logm().error(type(self).__name__ + ": ---ChunkedEncodingError---")
        except:
            self._logm().error(type(self).__name__ + ": ---UnknownError---")
