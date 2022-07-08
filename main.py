from multiprocessing import Process
import os
import requests
import configparser
import time
from urllib import request

# 具体端口设计在main.ini中
config = configparser.ConfigParser()
config.read('./main.ini')
flask_port = config.getint('flask', 'port')
http_port = config.getint('go-cqhttp', 'port')


def go_cqhttp():
    os.system("python go-cqhttp.py")


def server():
    os.system("nohup python server.py > ./logs/flask.log 2>&1 &")

def Listening_Pro():
    pass

if __name__ == '__main__':
    process_list = []
    p_s = Process(target=server, args=())
    p_s.start()
    Flag = True
    INDEX_URL = "http://127.0.0.1:" + str(flask_port) + "/test"
    while True:
        try:
            request.urlopen(url=INDEX_URL)
            break
        except Exception as e:
            time.sleep(0.5)
    print('Flask Server started ! Log in ./logs/flask.log ......')
    p_g = Process(target=go_cqhttp, args=())
    p_g.start()
    print("message dealing...")
    address = "http://127.0.0.1:" + str(http_port)
    T=time.time()
    while (1==1):
        time.sleep(0.5)
        temp = time.time()
        if ((temp-T) % 60 >= 0 and (temp-T) % 60 <= 1):
            print(temp-T)
        if (temp-T>=898 and temp-T<=902):
            T=temp
            print(T,temp)
            try:
                requests.get(
                    url=address + '/send_private_msg?user_id={0}&message={1}'.format("2463645141", "蠢货赶紧写作业啦"))
            except requests.exceptions.ConnectionError:
                print('ConnectionError -- please wait 5 seconds')
            except:
                print('Unfortunitely -- An Unknow Error Happened, Please wait 5 seconds')
            time.sleep(3)
            print(T, temp)
            time.sleep(5)
