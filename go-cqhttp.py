import yaml
import os
import configparser
import time

config = configparser.ConfigParser()
config.read('./main.ini')                                   # 读取配置文件
print("Checking Go-CQhttp...")
if not(os.path.exists("./go-cqhttp/go-cqhttp")):            # 如果go-cqhttp不存在，则向用户要求下载
    print("[FAIL] No Go-CQHTTP Found! \n Please download go-cqhttp corresponding to the platform to the go-cqhttp Fold first!")
    time.sleep(1)
    os.exit()
    
if (os.path.exists("./go-cqhttp/config.yml")):              # 如果config.yml存在，则读取config.yml
    print("[OK] Find go-cqhttp Configuration")
else:
    print("[FAIL] No go-cqhttp Configuration......")
    time.sleep(1)
    exit()
    
yamlPath = "./go-cqhttp/config.yml"

with open(yamlPath, 'r', encoding='utf-8') as file:
    result = file.read()
    bot_yml = yaml.safe_load(result)
    qq_num = int(input("Enter your QQ Number:"))            # 输入QQ号码
    qq_passwd = str(
        input("Enter your QQ password(if is empty then will scan the QRcode):"))        # 输入QQ密码（如果没有密码那么扫描二维码登陆）
    http_port = config.getint('go-cqhttp', 'port')
    flask_port = config.getint('flask', 'port')
    print("For more go-cqhttp Configuration, Edit the ./config.yml ......")
    bot_yml["account"]["uin"] = qq_num
    bot_yml["account"]["password"] = qq_passwd
    bot_yml["servers"][0]["http"]["port"] = http_port
    bot_yml["servers"][0]["http"]["post"][0]["url"] = "http://127.0.0.1:" + \
        str(flask_port)
    bot_yml["servers"][0]["http"]["post"][0]["secret"] = ""
    with open(yamlPath, 'w', encoding='utf-8') as write_file:
        yaml.dump(bot_yml, write_file)

print("Starting go-cqhttp Server on port...... ")
os.system("cd go-cqhttp && ./go-cqhttp")                    # 启动go-cqhttp服务
