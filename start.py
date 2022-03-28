import yaml
import os

if (os.path.exists("./config.yml")):
    print("Find go-cqhttp Configuration......")
else:
    print("No go-cqhttp Configuration......")
    os.system("pause")
    exit()
yamlPath = "./config.yml"
# with open(address, 'w', encoding='utf-8') as write_file:
#    http_port = str(input("Enter your HTTP port:"))
#    write_file.write("127.0.0.1:" + http_port)


with open(yamlPath, 'r', encoding='utf-8') as file:
    result = file.read()
    bot_yml = yaml.safe_load(result)
    print(bot_yml)
    qq_num = int(input("Enter your QQ Number:"))
    qq_passwd = str(
        input("Enter your QQ password(if is empty then will scan the QRcode):"))
    http_port = int(input("Enter your http port:"))
    print("For more go-cqhttp Configuration, Edit the ./config.yml ......")
    bot_yml["account"]["uin"] = qq_num
    bot_yml["account"]["password"] = qq_passwd
    bot_yml["servers"][0]["http"]["port"] = http_port
#    bot_yml["servers"][0]["http"]["post"][0]["url"]=str("127.0.0.1:8880")
#    bot_yml["servers"][0]["http"]["post"][0]["secret"]=""
    with open("./port.txt", 'w', encoding='utf-8') as write_file:
        write_file.write(str(http_port))
    with open(yamlPath, 'w', encoding='utf-8') as write_file:
        yaml.dump(bot_yml, write_file)

print("Starting go-cqhttp Server on port......")
os.system("./go-cqhttp/go-cqhttp fastboot")
