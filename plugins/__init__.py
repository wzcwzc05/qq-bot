import os
import json
print("Initing Plugins......")

#获取当前路径



def GetAllKeys(path):
    pass


def GetAllPlugins():
    File=os.listdir()
    plugins_dir = []
    for i in File:
        if (os.path.isdir("./"+i)):
            plugins_dir.append(i)
    return plugins_dir

print(GetAllPlugins())
if __name__=='__main__':
    plugins = GetAllPlugins()
    for i in plugins:
        pass
        
__all__ = ['api/api.py']
