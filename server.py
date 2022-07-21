from flask import Flask, request
import plugins
import configparser
import os
import signal


config = configparser.ConfigParser()
config.read('./main.ini')
http_port = config.getint('go-cqhttp', 'port')      # 获取go-cqhttp的端口
app = Flask(__name__)


@app.route('/', methods=["POST"])           # 接受go-cqhttp发送的消息
def post_data():
    if request.get_json().get('message_type') == 'private':
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        # 发送调用plugins.api.enterance函数，进入插件系统
        plugins.api.enterance(http_port, message, uid)

    if request.get_json().get('message_type') == 'group':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        # 发送调用plugins.api.enterance函数，进入插件系统
        plugins.api.enterance(http_port, message, uid, gid)

    return "None"


@app.route('/test')             # 测试是否启动
def test_pass():
    return "Success"


@app.route("/stop")             # 停止服务
def stop():
    os._exit(0)


if __name__ == '__main__':
    flask_port = config.getint('flask', 'port')
    app.run(debug=True, host='0.0.0.0', port=flask_port)        # 启动flask服务
