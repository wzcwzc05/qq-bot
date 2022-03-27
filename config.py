from ipaddress import ip_address
import yaml
import os

if (os.path.exists("./go-cqhttp/config.yml")):
    print("Find go-cqhttp Configuration......")
else:
    print("No go-cqhttp Configuration......")
    print("First Starting go-cqhttp......")
    os.system('./go-cqhttp/go-cqhttp')
    if (os.path.exists("./go-cqhttp/config.yml") == False):
        print("Generating Config Failed! Exiting ......")
        os.system("pause")
        exit()
yamlPath = "./go-cqhttp/config.yml"
address = "./go-cqhttp/address.txt"


with open(address, 'w', encoding='utf-8') as write_file:
    http_port = str(input("Enter your HTTP port:"))
    write_file.write("0.0.0.0:" + http_port)


with open(yamlPath, 'r', encoding='utf-8') as file:
    result = file.read()
    bot_yml = yaml.load(result, Loader=yaml.FullLoader)
    qq_num = int(input("Enter your QQ Number:"))
    qq_passwd = str(
        input("Enter your QQ password(if is empty then will scan the QRcode):"))
    print("For more go-cqhttp Configuration, Edit the ./go-cqhttp/config.yml ......")
    bot_yml["account"]["uin"] = qq_num
    bot_yml["account"]["password"] = qq_passwd
    with open(yamlPath, 'w', encoding='utf-8') as write_file:
        yaml.dump(bot_yml, write_file)

