# -*- coding: utf-8 -*-
# @Time : 2022/8/18 12:48
# @Author : joel
# @Email : 770546904@qq.com
# @File : mysql_test.py
"""
@Filename: /mysql_test
@Describe: ...
"""

import pymysql as MySQLdb


class DBServer:

    def __init__(self, *args, **kwargs):
        self.db = MySQLdb.connect(*args, **kwargs)
        self.c = self.db.cursor()

    def sql_execute(self, sql):
        self.c.execute(sql)
        res = self.c.fetchone()
        # res = self.c.fetchall()
        return res


if __name__ == '__main__':
    db = DBServer(
        host='10.0.3.243',
        port=13306,
        database='zhangin_vspex',
        user='zhangin_vspex',
        password='zhangin18vspex',
    )

    res = db.sql_execute("SELECT * FROM yx_seal WHERE seal_mac = 'E07DEA736C06'")
    print(res)
