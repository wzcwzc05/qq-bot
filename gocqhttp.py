import yaml
import os
import configparser
import time

def StartGoCQhttp():
    config = configparser.ConfigParser()
    config.read('./main.ini')                                   # 读取配置文件
    print("Checking Go-CQhttp...")
    if not(os.path.exists("./go-cqhttp/go-cqhttp")):            # 如果go-cqhttp不存在，则向用户要求下载
        print("[FAIL] No Go-CQHTTP Found! \n Please download go-cqhttp corresponding to the platform to the './go-cqhttp' Fold first!")
        time.sleep(1)
        os.exit()

    print("Starting go-cqhttp Server on port...... ")
    os.system("cd go-cqhttp && ./go-cqhttp")                    # 启动go-cqhttp服务
