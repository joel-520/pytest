# -*- coding: utf-8 -*-
# @Time : 2022/9/16 13:26
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: commons/databases
# @Describe: ...
import pymysql


def create_connection():
    conn=pymysql.connect(
        user="root",
        password="123456",
        host="localhost",
        database="test",
        port=3306
    )
    return conn

def execute_sql(sql):
    cn = create_connection()
    cs = cn.cursor()
    cs.execute(sql)
    values = cs.fetchall()
    cs.close()
    cn.close()
    return values
if __name__ == '__main__':
    print(execute_sql("select test_title from test_t"))