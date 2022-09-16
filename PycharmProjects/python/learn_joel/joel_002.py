# -*- coding: utf-8 -*-
# @Time : 2022/8/8 14:43
# @Author : joel
# @Email : 770546904@qq.com
# @File : joel_002.py
"""
@Filename: /test_002
@Describe: ...
"""

# 通过类 设计一种动物，他们应该用于不同的名字、体重、身高，每个动物都可以计算出自己的BMI
# class Animal:
#     name = " "
#     weight = 0
#     height = 0
#
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#
#     def bmi(self):
#         bmi = float(self.weight) / float(self.height * 2)
#         return bmi
#
#
# a1 = Animal("a1",100,100)
# a2 = Animal("a2",100,160)
# a3 = Animal("a3",150,180)

# print(f"{a1.name}的BMI是{a1.bmi()}")
# print(f"{a2.name}的BMI是{a2.bmi()}")
# print(f"{a3.name}的BMI是{a3.bmi()}")


# class A:
#     pass
#
#
# def hello() -> object:
#     return "Hello, world!"
#
#
# A.hello = hello()
# print(A.hello)


# class Joel():
#
#     def a(self, *args, **kwargs):  # 实例方法
#         print(self, args, kwargs)
#
#     @classmethod  # 类方法
#     def b(self, *args, **kwargs):
#         print(self, args, kwargs)
#
#     @staticmethod  # 静态方法
#     def c(*args, **kwargs):
#         return args, kwargs
#         print(args, kwargs)
#
# joel = Joel()
#
# joel.a("abc", a="bmi")
# joel.b("123", b="666")
# print(joel.c("888", c="999"))


# class A:
#     name = "aa"
#     _age = 0
#
#     def say(self):
#         print(f"I am {self.name} and {self._age} years old.\n")
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         # return self._age
#         assert value > 0
#         self._age = value

# class B(A):
#
#     def b_say(self):
#         print(f"I am {self.name} and {self._age} years old.\n")
#         return 123

# a = A()
# print(a.name)
# a.age = -100
# print(a.age)
# print(a.say())

# b = B()
# print(b.name)
# b.age = 100
# print(b.age)
# print(b.b_say())


from datetime import datetime


# def logs(func):
#
#     def f(*args, **kwargs):
#         print(datetime.now(),func.name,"开始调用")
#         func(*args, **kwargs)
#         print(datetime.now(),func.name,"调用结束")
#     return f
#
# # logs()
#
# def add(x,y):
#     print("add is calling",f"{x=},{y=}")
#
# add(1,2)


# class Dog:
#     _msg = "汪汪"
#
#     def say(self):
#         return self._msg
#
#
# class Cat:
#     # @property
#     def say(self):
#         return '喵喵'
#
#
# def say(obj):
#     print(obj.say())
#
#
# say(Dog())
#
# say(Cat())


# class A:
#     class_name = "A"  # 类的属性
#
#     def __init__(self, name, age):
#         self.name = name  # 实例的属性
#         self.age = age  # 实例的属性
#
#     def show_me(self):
#         print(f"Hello，我的name是{self.name}")
#         print(f"Hello，我的age是{self.age}")
#
# a = A("北凡", 18)
# a.show_me()
#
#
# # 类A 进行【扩展】：增加一个 国家 属性
# class B(A):  # 继承实现扩展
#
#     def __init__(self, country, *args, **kwargs):
#         self.country = country
#         super().__init__(*args, **kwargs)  # 通过超类，实现对父类代码复用
#
# b = B(country='China', name="北凡", age=18)
# b.show_me()


# 创建一个装饰器，用校验【被装饰函数】收到的参数是否包含关键字参数，如果是，则打印：  Error：调用本函数时，只能传递位置参数

# def checkargs(func):
#     def inner(*args, **kwargs):
#
#         if kwargs:
#             print('Error：调用本函数时，只能传递位置参数')
#             # raise ValueError()
#         else:
#             return func(*args, **kwargs)
#
#     return inner
#
#
# @checkargs
# def foo(x, y):
#     return x + y
#
#
# print(foo(2, 3))
# print(foo(2, y=5))

# def checkargs(param_to_check):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             if param_to_check in kwargs:
#                 print('Error：调用本函数时，只能传递位置参数')
#             else:
#                 print('通过固定参数传递')
#             result = func(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return inner
#
#
# @checkargs(param_to_check='y')
# def foo(x, y):
#     return x + y
#
#
# print(foo(2, 3))
# print(foo(2, y=3))

# 创建一个生成器，用模拟和代替内置的range函数
# class GenRange():
#     """使用生成器模拟range函数"""
#
#     def __init__(self, start, end):
#         """通过构造函数传范围的值"""
#         self.start = start - 1
#         self.end = end
#
#
#     def get_num(self):
#         """
#         生成数
#         遇到yield程序会暂停执行，直到下次被唤醒，在执行一次
#         """
#         while True:
#             if self.start >= self.end - 1:
#                 break
#             self.start += 1
#             yield self.start
#
#
# gen = GenRange(5, 10).get_num()
# print(gen)  # 返回一个对象
# print(list(gen))  # 强制转换成列表形式

# def func(start, end):
#     start -= start
#     while True:
#         if start >= end-1:
#             break
#         start = start + 1
#         yield start
#
# f=func(2,5)
# print(f)
# print(list(f))


# def my_range(start, stop=None, step=None):
#     if stop is None and step is None:  # 说明只有start 收到了参数 （只接收一个参数）
#         start, stop = stop, start  # start 和 stop 互换
#     if start is None:
#         start = 0
#     if stop is None:
#         stop = 0
#     if step is None:
#         step = 1
#     if stop == 0:
#         return
#     while True:
#         yield start
#         start = start + step
#         if start >= stop:
#             break

#
# class Person:
#     def __init__(cjavapy, name, age):
#         cjavapy.name = name
#         cjavapy.age = age
#
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)
#
# p1 = Person("cjavapy", 3)
# p1.myfunc()

# !/usr/bin/python

# var1 = 'helloworld!'
# var2 = "Python cjavapy"
#
# # print("var1[0]: ", var1[0])
# # print("var2[1:5]: ", var2[1:5])
# print(var1.capitalize())
# print(var1.casefold())
# print(var1.center(8))


# class A:
#     name = "ZQQ"
#     age = 17
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # 基本信息
#     def show_base(self):
#         print(f'大家好，我叫{self.name}，今年{self.age}岁了')
#
#
# def like():
#     print(f"我的爱好是：喜欢帅哥！")
#
#
# fangfa = 'love'  # 定义方法名
# a = A(name='涨三', age=19)  # 实例化对象
# setattr(a, fangfa, like)  # 实例化对象中添加love的方法
# print('--------反射方式读取方法----------------')
# getattr(a, fangfa)()  # 读取方法中的属性
# print('----------面向对象方式读取-------------')
# a.love()  # 面向对象的形式读取方法
# a = hasattr(a, fangfa)
# print(f"判断方法是否存在，返回---{a}")
