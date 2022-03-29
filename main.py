from multiprocessing import Process
import os
import requests
import configparser
#具体端口设计在main.ini中

def go_cqhttp():
    os.system("python start.py")


def server():
    os.system("python server.py")


if __name__ == '__main__':
    process_list = []
    p_s = Process(target=server, args=())
    p_s.start()
    Flag = True
#    while (Flag
    p_g = Process(target=go_cqhttp, args=())
    p_g.start()
