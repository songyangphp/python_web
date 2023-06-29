# -*- coding: utf-8 -*-

import flask
import controller.login as login_controller

server = flask.Flask(__name__)


@server.route('/')
def miss():
    return "hello python"


@server.route('/login', methods=['get', 'post'])
def login():
    return login_controller.loginController().do_login()


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')
