# -*- coding : utf-8 -*-
from flask import request
from libs.response import success, error
from libs.db.mysql import mySql
from model.user import user_info
import hashlib


def do_login():
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
    userinfo = user_info(cursor.fetchone())

    if userinfo == {}:
        return error("用户不存在")

    if userinfo['password'] != hashlib.md5(password.encode()).hexdigest():
        return error("密码错误")

    return success("登录成功！", userinfo)
