import requests
import json

with open("./port.txt", 'r', encoding='utf-8') as file:
        http_port = int(file.read())
address = "http://127.0.0.1:" + str(http_port)

def keyword(http_port,message, uid, gid=None):
    address = "http://127.0.0.1:" + str(http_port)
    if message[0:4] == 'ping':
        if (gid == None):
            requests.get(
                url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, "别叫了，我在"))
    if (message[0:])
