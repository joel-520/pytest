# -*- coding: utf-8 -*-
# @Time : 2022/7/9 13:55
# @Author : joel
# @Email : 770546904@qq.com
# @File : try.py

name = "joel"
money = 55

try:
    print("我在学习自动化")
    print("我的名字叫{}".format(name))
    print("我的目标薪资是{:.2f}".format(money))

# 不确定捕获的类型，我们可以用Exception
except Exception as e:
    print(e)  # 打印异常信息
# except NameError as e:
#     print(e) #打印异常信息
else:
    print("没有捕获异常")

finally:
    print("不管有没有异常，我都会执行")
# raise异常类型（异常信息）主动抛出异常
raise NameError("name'a'is not defined")
