# qq-bot
QQ机器人，基于go-cqhttp和flask。

采用go-cqhttp进行与QQ协议的交互，同时flask监听上报事件。

正在开发阶段……无法使用。

预计实现的功能

- [ ] `./plugins`存放插件，采用模块化开发。

config.json:

```json
{
    "name": "test",
    "version": 1.0,
    "author": "wzcwzc05",
    "email": "wzcwzc0@outlook.com",
    "key": [
        "ping",
        "hello"
    ]
}
```

`key`即为调用关键词。

目录中`main.py`即为插件主题，具体实现正在构思……

- [ ] 加入守护进程，可以让进程后台运行
- [ ] 通过`remi`等跨平台GUI等第三方库实现GUI界面管理
- [ ] 对于错误进行更科学的管理
