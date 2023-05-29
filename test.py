# -*- coding: utf-8 -*-

# 引入包

import flask
import json

# 创建服务
server = flask.Flask(__name__)


@server.route('/login', methods=['post', 'get'])
def login():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')
    if (not username) or (not password):
        return json.dumps({"code": 500, "msg": "参数错误"})

    return json.dumps({"code": 200, "msg": "登录成功"})


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')
