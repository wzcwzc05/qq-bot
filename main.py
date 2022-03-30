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
    os.system("python start.py")


def server():
    os.system("nohup python server.py > ./logs/flask.log 2>&1 &")


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
    
