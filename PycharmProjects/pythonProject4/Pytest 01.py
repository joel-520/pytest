# -*- coding: utf-8 -*-

# Pytest参数说明
# -v 说明：可以输出用例更加详细的执行信息，比如用例所在的文件及用例名称等
#
# -s 说明：输入我们用例中的调式信息，比如print的打印信息等
#
# -x：遇到错误的用例，立即退出执行，并输出结果
#
# -v：表示查看详细的报告内容
#
# -collect-only：表示把待执行的用例全部展示出来
#
# -lf：只执行上次失败的用例
#
# -vv ：显示详细的测试结果
#
# -tb=no：不展示用例失败的错误详情
#
# -tb=line：展示用例失败的代码具体行数
#
# -tb=short：展示更加详细的错误信息
#
# -k “关键字” 说明：执行用例包含“关键字”的用例
#
# -q 说明：简化控制台的输出，可以看出输出信息和上面的结果都不一样， 下图中有两个…点代替了pass结果
#
# -maxfail=num 当用例错误达到指定数量时，停止测试
#
# m 说明：执行特定的测试用例。我们再次修改一下我们的用例，并添加一个新的用例
#
# # 如果要运行多个标识的话，用表达式，如下
# pytest -m "slow or faster" test_1.py  运行有slow标识或 faster标识用例
# pytest -m "slow and faster" test_1.py 运行有slow和faster标识的用例
# pytest -m "slow and not faster" test_1.py 运行有slow和没有faster标识的用例
# 注意：-m后面不能带’'号（单引号），只能带“”（双引号），不然识别不到


import pytest
pytest.main(["test.py"])

#跳过测试函数： 根据特定的条件，不执行标识的测试函数
class Test():
   def test(self):
       print("执行的是testcase的用例")

@pytest.mark.skipif(condition=1<2,reason="1不大于2，所以不执行")
class huace():
   def haha(self):
       print("执行的是haha方法里面的用例")


# -*- coding: utf-8 -*-
#fixtur当做参数传入
import pytest

@pytest.fixture()
def login():
   print('登录系统')

# 直接使用函数名做为参数传入
def test_01(login):
   print('测试用例一')

def test_02():
   print('测试用例2')

def test03():
   print('测试用例3')

#fixture语法
# scope有4个作用范围：function(不填则默认)、class、module、session
#fixture(scope='function', params=None, autouse=False, ids=None, name=None)

# 参数说明
# scope：即作用域，function"（默认），“class”，“module”，"session"四个
#
# params：可选参数列表，它将导致多个参数调用fixture函数和所有测试使用它。
#
# autouse：默认：False，需要用例手动调用该fixture；如果是True，所有作用域内的测试用例都会自动调用该fixture
#
# ids：params测试ID的一部分。如果没有将从params自动生成.
#
# name：默认：装饰器的名称，同一模块的fixture相互调用建议写个不同的name。
#
# session的作用域：是整个测试会话，即开始执行pytest到结束测试scope参数作用范围控制fixture的作用范围：session>module>class>function


#创建pytest.ini文件(固定写法）
# [pytest];固定写法；变量名不能错
# addopts=-vv -s ；多个参数中间空格
# testpaths=../HC/huace ；多个目录中间空格
# python_files=test*.py ；python文件前缀，可自定义
# python_classes=huace ；指定类名
# python_functions=test* ;指定方法名,可自定义




