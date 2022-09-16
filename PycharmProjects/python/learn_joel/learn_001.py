# -*- coding: utf-8 -*-
# @Time : 2022/8/16 9:24
# @Author : joel
# @Email : 770546904@qq.com
# @File : learn_001.py
"""
@Filename: /learn_001
@Describe: ...
"""

# class Person(object):
#     def __init__(self, name, age=None, birthday=None):
#         self.name = name
#         self.age = age
#         self.birthday = birthday
#
#     def f(self):
#         print('我的名字{}，{}岁，生日是{}'.format(self.name, self.age, self.birthday))
#
# p = Person('joel', 18, '0208')
# p.age = -9
# p.f()
# print(p.f)


# import math
#
# print(dir(math))

# x = "555666888"
# print(x.index('888'))
# print(isinstance(x, float))

# thisdict = {
#     # "name": "cjavapy",
#     "age": 3,
#     "gender": "man"
# }
# thisdict["age"] = 5
# print(thisdict["age"])
# print(thisdict)

# for x in thisdict:
# print(x)
# print(thisdict[x])


# for x in thisdict.values():
#     print(x)
#     # print(thisdict[x])
#     print(type(x))


# for x,y in thisdict.items():
#     print(x,y)

# if "name" in thisdict:
#     print("'name'存在这个字典中")
#
# else:
#     print("不在这个字典中")
# d=thisdict.copy()
# print(f"{d=}")
#
# myd=dict(d)
# print(f"{myd=}")

# thisdict['addres']="224"
# print(thisdict)
#
# thisdict.pop('addres')
# print(thisdict)
#
# del thisdict['age']
# print(thisdict)
#
# thisdict.clear()
# print(thisdict)

# i = 0
# while i < 10:
#     i += 1
#
#     if i == 5:
#         # break
#         continue
#     print(i)
# else:
#     print('i不小于10')


# import datetime
#
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%m"))
#
# x = datetime.datetime(2020, 5, 17)
#
# print(x)

# coding:utf-8
# from datetime import *
#
# dt = datetime.now()
# # 日期减一天
# dt1 = dt + timedelta(days=-1)  # 昨天
# dt2 = dt - timedelta(days=1)  # 昨天
# dt3 = dt + timedelta(days=1)  # 明天
# delta_obj = dt3 - dt
# print(dt1,dt2,dt3)
# print(type(delta_obj), delta_obj)  # <type 'datetime.timedelta'> 1 day, 0:00:00
# print(delta_obj.days, delta_obj.total_seconds())  # 1 86400.0

# x = min(5, 10, 25)
# y = max(5, 10, 25)
# min()
# max()
# abs()
# pow()
# pow
# print(x)
# print(y)
# x = abs(-7.25)
#
# print(x)
#
# x = pow(4, 3)
#
# print(x)

# import math
#
# x = math.sqrt(64)
#
# print(x)
import math
# math.sqrt
# math.ceil()
# math.floor()
#
# x = math.ceil(1.4)
# y = math.floor(1.4)
#
# print(x) # returns 2
# print(y) # returns 1
# x = math.pi
#
# print(x)

import json

# x =  '{ "name":"cjavapy", "age":3, "city":"china"}'
#
# # 解析 x:
# y = json.loads(x)
#
# print(y["name"])

# a Python object (dict):
# x =  { "name":"cjavapy", "age":3, "city":"china"}
#
#
# # convert into JSON:
# y = json.dumps(x)
#
# #结果是 JSON string:
# print(y)
#
# print(json.dumps({"name": "cjavapy", "age": 3}))
# print(json.dumps(["python", "cjavapy"]))
# print(json.dumps(("python", "cjavapy")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# x = {
# "name": "python",
# "age": 20,
# "married": True,
# "divorced": False,
# "children": ("c","python"),
# "pets": None,
# "langs": [
# {"model": "java", "year": 5},
# {"model": "python", "year": 6}
# ]
# }
# print(json.dumps(x, indent=2))
# print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x, indent=4, separators=(". ", " = "),sort_keys=True))
# print(json.dumps(x,sort_keys=True))


# import regex as re
#
# txt = "The website is cjavapy"
# x = re.search("^The.*py$",txt)
#
# print(x)
#
# txt = "myname is cjavapy"
# x = re.search("\s", txt)
#
# print("第一个空白字符位置:", x.start())
# txt = "my name is cjavapy"
# x = re.split("\s", txt)
# x = re.split("\s", txt,2)
#
# print(x)
# txt = "my name is cjavapy"
# x = re.sub("\s", "7", txt)
# x = re.sub("\s", "7", txt,2)
# print(x)
#
# txt = "my name is Cjavapy"
# x = re.search(r"\bC\w+", txt)
# print(x.span())
# print(x.string)
# print(x.group())


# def find_char(s):
#     if len(s)==0:
#         return " "
#     visited=[]
#     for i in range(len(s)):
#         if s[i] not in visited:#s[i]不在遍历过的字符里
#             visited.append(s[i])
#             if s[i] not in s[i+1:]:#s[i]不在未遍历的字符里
#                 return s[i]
#     return " "
# # s="abaccdeff"
# # s="aabbccdd"
# s=" "
# print(find_char(s))

# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# l = [1, 2, 3, 4]
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and i != k and j != k:
#                 print(i, j, k)

    #     print()
    # print()

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
# 　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
# 　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
# 　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# bonus1 = 100000 * 0.1
# bonus2 = bonus1 + 100000 * 0.500075
# bonus4 = bonus2 + 200000 * 0.5
# bonus6 = bonus4 + 200000 * 0.3
# bonus10 = bonus6 + 400000 * 0.15
#
# i = int(input('请输入当月利润:\n'))
#
# if i <= 100000:
#     bonus = i * 0.1
# elif i <= 200000:
#     bonus = bonus1 + (i - 100000) * 0.075
# elif i <= 400000:
#     bonus = bonus2 + (i - 200000) * 0.05
# elif i <= 600000:
#     bonus = bonus4 + (i - 400000) * 0.03
# elif i <= 1000000:
#     bonus = bonus6 + (i - 600000) * 0.015
# else:
#     bonus = bonus10 + (i - 1000000) * 0.01
# print('bonus = ',bonus)
