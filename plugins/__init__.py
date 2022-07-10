import json
import time
import os

with open("./plugins/plugins.json", 'r') as load_f:
    PluginsData = json.load(load_f)
PluginsList = []

print("Updateing plugins...")
DirList = os.listdir("./plugins")
PluginsLoad = []
for i in DirList:
    if (os.path.isdir("./plugins/"+i) == True) and (i!="__pycache__"):
        PluginsLoad.append(i)
for plugin in PluginsLoad:
    with open("./plugins/"+plugin+"/conf.json", 'r') as load_f:
        plugin_data = json.load(load_f)
    print("Loading plugin: " + plugin_data["name"]+" from fold "+plugin)
    PluginsList.append(plugin_data)
    
PluginsData["plugins"] = PluginsList
with open("./plugins/plugins.json", 'w') as dump_f:
    json.dump(PluginsData, dump_f)
    
print("Checking Plugins...")
with open("./plugins/plugins.json", 'r') as load_f:
    PluginsData = json.load(load_f)
PluginsList = PluginsData["plugins"]

for i in PluginsList:
    if (i["active"]==True):
        print("name:",i["name"], i["version"], "type:",i["type"])
time.sleep(1.5)

__all__ = ["api", "ClassMain"]
