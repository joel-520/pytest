# -*- coding: utf-8 -*-
# @Time : 2022/7/9 10:57
# @Author : joel
# @Email : 770546904@qq.com
# @File : 数据库.py

# -*- coding: utf-8 -*-
__author__ = "苦叶子"
import unittest

from sqlalchemy import create_engine
from sqlalchemy.engine import reflection


class TestMySQL(unittest.TestCase):
    def setUp(self):
        # 创建连接
        self.engine = create_engine("mysql+pymysql://root:12345678@127.0.0.1:3306/mysql")

        # 创建inspector对象
        self.insp = reflection.Inspector.from_engine(self.engine)

    def test_table_name(self):
        # 判断user表是否在mysql这个实例库中
        self.assertIn("user", self.insp.get_table_names())

    def test_column(self):
        # user表中是否有User字段
        User = None
        columns = self.insp.get_columns("user")
        for col in columns:
            if "User" == col["name"]:
                User = col["name"]

        self.assertIsNotNone(User)

    def test_keyprimary(self):
        # 验证user表中User字段是否为主键
        k = self.insp.get_pk_constraint("user")
        self.assertIn("User", k["constrained_columns"])


if __name__ == "__main__":

    unittest.main()