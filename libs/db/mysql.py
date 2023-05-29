# -*- coding : utf-8 -*-

import pymysql

host = "127.0.0.1"
user = "root"
password = "654321"
database = "epii"


class mySql:
    def get_cursor(self):
        db = pymysql.connect(host=host, user=user, database=database, password=password)
        cursor = db.cursor()
        return cursor
