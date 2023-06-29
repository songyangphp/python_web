# -*- coding : utf-8 -*-
from flask import request
from libs.response import success, error
from libs.db.mysql import mySql
import model.user as user_model
import hashlib
from libs.cache import redis_cache
import json


class loginController:
    # 简单demo
    def do_login(self):
        username = request.values.get("username")
        password = request.values.get("password")
        if username is None:
            return error("请输入用户名")
        if password is None:
            return error("请输入密码")

        sql = "SELECT * FROM `epii_admin` WHERE `username` = '%s'" % username
        # return error(sql)
        cursor = mySql().get_cursor()
        cursor.execute(sql)
        userinfo = user_model.user_info(cursor.fetchone())

        if userinfo == {}:
            return error("用户不存在")

        if userinfo['password'] != hashlib.md5(password.encode()).hexdigest():
            return error("密码错误")

        # print(str(userinfo['id'])+'songyang')
        token = hashlib.md5((str(userinfo['id']) + 'songyang').encode()).hexdigest()
        cache = redis_cache.redisCache().get_drive()
        cache.set("song_test_" + token, json.dumps(userinfo))

        response_data = {'token': token}
        return success("登录成功！", response_data)
