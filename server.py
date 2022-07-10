from flask import Flask, request
from plugins import *
import configparser

config = configparser.ConfigParser()
config.read('./main.ini')
http_port = config.getint('go-cqhttp', 'port')
app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        api.enterance(http_port, message, uid)

    if request.get_json().get('message_type') == 'group':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        api.enterance(http_port, message, uid, gid)

    return "None"


@app.route('/test')
def test_pass():
    return "Success"

if __name__ == '__main__':
    flask_port = config.getint('flask', 'port')
    app.run(debug=True, host='0.0.0.0', port=flask_port)
