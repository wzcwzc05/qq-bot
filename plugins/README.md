# 插件系统

插件系统工作原理与如何自己开发插件

## 一、基本配置

每一个插件视作一个python模块进行调用，应遵循如下规则：

### 1.文件组成

文件插件文件夹中应包含如下文件

```bash
-PluginName
    __init__.py    # 模块初始化
    main.py        # 执行脚本
    conf.json        # 插件配置
```

### 2.插件配置

以自带的example插件为例：

conf.json:

```json
{
    "name": "example",
    "entry": "main",
    "active": true,
    "version": "1.0.0",
    "description": "example plugin",
    "author": "test",
    "type": "command",
    "commands": {
        "IsGroup": false,
        "IsPrivate": true,
        "uid": [],
        "gid": [],
        "strict": true,
        "words": [
            "ping"
        ]
    }
}
```

- “name”:插件名称。
  
  > 注意！插件名称应与 **文件夹名称** 、 **子类名** 相同

- “entry”：入口，例如“main.py”

- "active"：插件是否激活

- “version”、“description”、“author”：版本、插件描述、作者

- “type”：插件类型，分为“command”与“persistence”，下一章节具体介绍。
