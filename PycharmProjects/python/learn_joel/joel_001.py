# -*- coding: utf-8 -*-
# @Time : 2022/8/8 10:03
# @Author : joel
# @Email : 770546904@qq.com
# @File : joel_001.py
# @Filename: /test_001
# @Describe: ...


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
# a1 = Animal("a1", 60, 1.75)
# a2 = Animal("a2", 90, 1.75)
# a3 = Animal("a3", 150, 170)


# a1.name = "a1"
# a1.weight = 50
# a1.height = 1.60
#
# a2.name = "a2"
# a2.weight = 60
# a2.height = 1.60
#
# a3.name = "a3"
# a3.weight = 80
# a3.height = 1.80

# print(f"{a1.name}的BMI是{a1.bmi()}")
# print(f"{a2.name}的BMI是{a2.bmi()}")
# print(f"{a3.name}的BMI是{a3.bmi()}")

# s="abn"
# a="lll"
# print(s.join(a))
# import time


# import datetime
#
#
# now1=datetime.datetime.today()
# now2=datetime.datetime.now()
# now3=datetime.datetime.date(self=now1)
# now4=datetime.datetime.day
# now5=datetime.datetime.hour
# now6=datetime.datetime.minute
# now7=datetime.datetime.second
# now9=datetime.datetime.microsecond

# print(now1, now2, now4, now5, now6, now7, now9,sep="\n")
# name = "H"
#
# def call(f, *args, **kwargs):
#     name = "456"
#     return name,f(*args, **kwargs)
#
#
# # def f(*args, **kwargs):
# #     name = "123"
# #     return name
#
#
# print(print, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep="\n")


# a = [[1, 3, 2]]
# b = a * 3
# b[0][0] = 20
# print(b)


# L=[i for i in range(30) if i % 3 == 0]
# print(L)

# 根据面向对象的特性，创建一个可以被say函数作为参数的 Cat类，使以下代码执行正确

# class Dog:
#     _msg = "汪汪"
#
#     def say(self):
#         return self._msg
#
#
# class Cat(Dog):
#     pass
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
#     name = "aa"
#     _age = 0
#
#     def say(self):
#         print(f"I am {self.name},{self._age} years old")
#         return self.name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         self._age = value
#
#
# a = A()
# # a.name = "66"
# a.age = 1
# print(a.age)
# print(a.say())


# class A:
#     name = "aa"
#     __age = 0
#
#     def say(self):
#         print(f"I am {self.name},{self.__age} years old")
#         return self.name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         assert value > 0
#         self.__age = value
#
#
# class B(A):
#
#
#
#     def b_say(self):
#         print(f"I am {self.name},{self.__age} years old")
#         return 123
#
#
# b = B()
# # a.name = "66"
# b.age = 100
# print(b.age)
# print(b.say())


#
# class Man:
#     name = "无名氏"
#
#     def say(self):
#         print(self.name)
#
#
# class Message(Man):
#     pass
#
# man= Man()
# man.say()
#
# msg = Message()
# msg.say()



#
# a=[[1,2],[5,1],[3,5],[2,4]]
# a.sort(key=lambda x: x[1])
# print(a)


"""
使用python的迭代器和生成器模拟python内置的range函数
"""


# def use_range():
#     """python内置的range函数"""
#     for i in range(5, 10):
#         print(i)


class IterRange(object):
    """使用迭代器来模拟range()函数"""

    def __init__(self, start, end):
        """通过构造函数传范围的值"""
        self.start = start - 1

        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class GenRange(object):
    """使用生成器模拟range函数"""

    def __init__(self, start, end):
        """通过构造函数传范围的值"""
        self.start = start - 1
        self.end = end

    def get_num(self):
        """
        生成数
        遇到yield程序会暂停执行，直到下次被唤醒，在执行一次
        """
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start


def get_num(start, end):
    """用函数的方式使用生成器实现range函数"""
    start -= 1
    while True:
        if start >= end - 1:
            break
        start += 1
        yield start


if __name__ == '__main__':
    # 演示内置range函数
    # use_range()

    # 迭代器实现range用列表返回
    iter_num = IterRange(5, 10)
    # print(next(iter_num))
    # print(next(iter_num))
    # print(next(iter_num))
    # print(next(iter_num))
    # print(next(iter_num))
    # 生成一个列表
    l1 = list(iter_num)
    print(l1)
    print("-----------------")

    # 生成器模拟range并返回列表
    gen = GenRange(5, 10).get_num()
    print(gen)  # 返回一个对象
    print(list(gen))  # 强制转换成列表形式

    print("-----------------")
    gen_temp = get_num(5, 10)
    print(gen)  # 返回一个对象
    print(list(gen_temp))































