import requests
import json
from plugins import MainClass

def enterance(http_port, message, uid, gid=None):
    address = "http://127.0.0.1:" + str(http_port)
    if message[0:4] == 'ping':
        if (gid == None):
            requests.get(
                url = address + '/send_private_msg?user_id={0}&message={1}'.format(uid, "别叫了，我在"))
        elif (gid != None):
            requests.get(
                url = address + '/send_group_msg?group_id={0}&message={1}'.format(gid, "别叫了，我在"))