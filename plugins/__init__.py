import json
import time
import os

def CheckPlugins(plugin):
    return True

if not(os.path.exists("./plugins/plugins.json")):                       # 如果插件总体配置文件不存在则报错
    print("[ERROR] The Configuration of plugin system isn't existed!")
    time.sleep(1)
    os._exit(0)
    
with open("./plugins/plugins.json", 'r') as load_f:                             # 读取插件系统总体配置文件
    PluginsData = json.load(load_f)
PluginsList = []

print("Updateing plugins...")
DirList = os.listdir("./plugins")
PluginsLoad = []
for i in DirList:
    if (os.path.isdir("./plugins/"+i) == True) and (i!="__pycache__"):          # 如果是文件夹且不是__pycache__那么就当作插件导入
        PluginsLoad.append(i)
for plugin in PluginsLoad:
    
    if not(os.path.exists("./plugins/"+plugin+"/conf.json")):                   # 如果插件配置文件不存在则忽略文件夹
        continue
    
    with open("./plugins/"+plugin+"/conf.json", 'r') as load_f:                 # 加载插件配置文件
        plugin_data = json.load(load_f)
    print("Loading plugin: " + plugin_data["name"]+" from fold "+plugin)
    PluginsList.append(plugin_data)
    
PluginsData["plugins"] = PluginsList
with open("./plugins/plugins.json", 'w') as dump_f:
    json.dump(PluginsData, dump_f)
    
print("[OK]")
time.sleep(0.5)
    
print("Checking Plugins...")                                                    # 检查插件是否有问题
with open("./plugins/plugins.json", 'r') as load_f:
    PluginsData = json.load(load_f)
PluginsList = PluginsData["plugins"]

for i in PluginsList:
    if (CheckPlugins(i) == False):
        print("[ERROR] Plugin: " + i["name"] + " is broken!")
        PluginsList.remove(i)
        continue
    
    if (i["active"]==True):
        print("name:",i["name"], i["version"], "type:",i["type"])
        __import__("plugins."+i["name"]+"."+i["entry"])
        
PluginsData["plugins"] = PluginsList
with open("./plugins/plugins.json", 'w') as dump_f:
    json.dump(PluginsData, dump_f)
            
print("[OK]")
time.sleep(1.5)
