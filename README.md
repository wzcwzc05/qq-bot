# qq-bot

QQ机器人，基于go-cqhttp和flask。

> **（开发未完成）**
> 
> 且对Windows无适配，现在仅能在Linux上运行

采用go-cqhttp进行与QQ协议的交互，同时flask监听上报事件。

预计实现的功能

- [x] `./plugins`存放插件，采用模块化开发。
- [x] 日志系统
- [x] “command”类型插件
- [ ] “persistence”类型插件
- [ ] 适配Windows
- [ ] 第一次运行项目时根据系统类型，自动下载go-cqhttp

## 一、项目运行

> 未来实现：第一次运行项目时根据系统类型，自动下载go-cqhttp
> 
> 现在仍需用户自行下载go-cqhttp可执行文件到go-cqhttp文件夹中。
> 
> 项目自带go-cqhttp为Linux x86 64位下的go-cqhttp 1.0.0-rc1版本

### 1.Linux

安装依赖库：`pip install configparser flask requests yaml`

运行项目：`python main.py`

> 注意：第一次运行时，go-cqhttp最好采用扫描二维码的方式登陆QQ

### 2.Windows

（Windows下尚未适配）

## 二、 项目目录

```bash
QQ-bot
    -go-cqhttp    # go-http目录
    -log            
        api.log    # api调用日志
        flask.log    # flask日志
        go-cqhttp.log    # go-cqhttp日志
    -plugins    # 插件目录
        -examples    # examples插件
        __init__.py
        ClassMain.py
        api.py
        plugins.json
        README.md    # 关于插件系统的详细介绍
    go-cqhttp.py    # 启动go-cqhttp
    server.py    # 启动flask
    main.py    # 项目入口
```

## 二、插件介绍

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
