from genericpath import exists
import os
import json
import sqlite3

print("Initing Plugins......")


def GetAllKeys(path):
    pass


def GetAllPlugins():
    File = os.listdir()
    plugins_dir = []
    for i in File:
        if (os.path.isdir("./"+i)):
            plugins_dir.append(i)
    return plugins_dir


print(GetAllPlugins())
if __name__ == '__main__':
    plugins = GetAllPlugins()
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    sql_text_1 = '''CREATE TABLE search
           (Name TEXT,
            Key TEXT);'''
    for i in plugins:           #更新插件索引
        if ((os.path.exists("./"+i+"/main.py")) and (os.path.exists("./"+i+"/config.json"))):
            print("Loading Plugin: "+i)
            with open("./"+i+"/config.json", "r") as f:
                config = json.load(f)
                Name = config.get("name")
                key = config.get("key")
                
        else:
            print("Plugin "+i+" is not valid")

__all__ = ['api/api.py']
