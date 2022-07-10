import json
import time

print("Checking Plugins...")
with open("./plugins/plugins.json", 'r') as load_f:
    PluginsData = json.load(load_f)
print(PluginsData)
PluginsList = PluginsData["plugins"]

for i in PluginsList:
    if (i["active"]==True):
        print("name:",i["name"], i["version"], "type:",i["type"])
time.sleep(1.5)

__all__ = ["api", "ClassMain"]
