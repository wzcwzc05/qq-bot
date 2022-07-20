# qq-bot

QQ机器人，基于go-cqhttp和flask。

采用go-cqhttp进行与QQ协议的交互，同时flask监听上报事件。



预计实现的功能

- [x] `./plugins`存放插件，采用模块化开发。

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
