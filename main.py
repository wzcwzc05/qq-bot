from multiprocessing import Process
import os
import requests
import configparser
import time
from urllib import request
import signal
import platform

# 具体端口设计在main.ini中
config = configparser.ConfigParser()
config.read('./main.ini')
flask_port = config.getint('flask', 'port')
http_port = config.getint('go-cqhttp', 'port')


def go_cqhttp():
    os.system("python go-cqhttp.py")


def server():
    os.system("nohup python server.py > ./logs/flask.log 2>&1 &")
    

def breakdown(e1, e2):
    print("Go-CQHTTP Server has stopped !")
    INDEX_URL = "http://127.0.0.1:" + str(flask_port) + "/stop"
    request.urlopen(url=INDEX_URL)
    time.sleep(0.5)
    print("QQ-bot has stopping...")
    p_s.terminate()
    time.sleep(1)
    exit()
    
if __name__ == '__main__':
    sysstr = platform.system()
    with open("./logs/api.log", 'w', encoding='utf-8') as write_file:
        write_file = ""

    if (sysstr == "Windows"):
        print("Windows isn't Fully Supported! Please manually run the server.py and go-cqhttp.py")
        os.system("pause")
        os.exit()
            
    signal.signal(signal.SIGINT, breakdown)         # Ctrl+C时触发go-cqhttp停止，同时停止flask服务
    
    print("Starting Listensing Server...")
    time.sleep(1)
    p_s = Process(target=server, args=())           # 启动flask服务
    p_s.start()
    
    Flag = True
    INDEX_URL = "http://127.0.0.1:" + str(flask_port) + "/test"
    while True:                                                 # 循环检测flask服务是否启动
        try:
            request.urlopen(url=INDEX_URL)
            break
        except Exception as e:
            time.sleep(0.5)
    print('Flask Server has started ! Log in ./logs/flask.log ......')
    time.sleep(1)
    
    p_g = Process(target=go_cqhttp, args=())                    # 启动go-cqhttp服务
    p_g.start()
    time.sleep(5)
    address = "http://127.0.0.1:" + str(http_port)
