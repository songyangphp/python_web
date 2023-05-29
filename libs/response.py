# -*- coding : utf-8 -*-

import datetime
import json


def success(msg='请求成功！', data=None):
    if data is None:
        data = []
    return json.dumps({"msg": msg, "data": data, "code": 200, "time": get_time()})


def error(msg='请求失败', code=500, data=None):
    if data is None:
        data = []
    return json.dumps({"msg": msg, "data": data, "code": code, "time": get_time()})


def get_time():
    return int(datetime.datetime.now().timestamp())
