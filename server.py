from flask import Flask, request
from api import api
with open("./port.txt", 'r', encoding='utf-8') as file:
    http_port = int(file.read())
app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        api.keyword(http_port, message, uid)

    if request.get_json().get('message_type') == 'group':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        api.keyword(http_port, message, uid, gid)

    return "None"
@app.route('/test')
def test():
    pass
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=8880)
