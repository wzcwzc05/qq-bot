import os
import json
print("Initing Plugins Success!")


def GetAllKeys():
    pass


def GetAllPlugins():
    File=os.listdir()
    plugins_dir = []
    for i in File:
        if (os.path.isdir("./"+i)):
            plugins_dir.append(i)
    return plugins_dir

print(GetAllPlugins())

__all__ = ['api']
