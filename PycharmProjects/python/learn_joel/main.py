# s = input("请输入内容：")
# print(s)
#
# print(input("请输入内容："))


# a = 100
# b = 10.0
#
# c = a -b
#
# print(c)
#
# b = int(b)
# a = float(a)
# print(a,b)


# s = "abcd"
# #
# # print(s)
# # print(s[0])      #打印整个字符串
# # print(s[1])      #根据下标值打印字符串
# # print(s[2])
# # print(s[3])
# #
# # #下标取值，从0开始 （用0表示第一个）
# # #下标取值，不能越界 （不能超过实际用于元素数量）
# #
# # print(len(s))   #获取最大长度
#
# #
# # s = "abcdefg"
# #
# # print((s[0], s[6 - 5]))   #正序打印
# # print((s[-1], s[- 5]))   #倒序打印
# #
# # #
# # # print(s[::])
# # # print(s[::-1])
# #
# #
# # print(s[0:-1:1])
# # #没有传递参数，就是默认参数
# #
# # print(s[::-1])
# # # print(s[4-1:6:2])
# # # 1. 有字符串 123456789 ，通过切片的方式，打印其中所有的偶数
# #
# # s = '123456789'
# # print(s[1::2])
#
# # 2. 有字符串 abcdefg ，通过基本输入获得下标序号，根据下标序号，打印对应的
# #
# # s= 'abcdefg'
# # i=int(input("请输入下标："))
# # print(s[i])
# # b = "abcdefg"
# # i = 5
# # s = "数据b(" + str(b) + ")中： 下标=" +str(i) + "时，值=" +str(b[i])
# # print(s)
#
#
# a = []
# a.append(1)
# a.append(1)
# a.extend([2,3,4])
# # a.insert(0,"joel")
# # a.insert(3,"test")
# # a.insert(-1,"ce")
# # a.pop()
# # a.pop(3)
# # a.remove("joel")
# # a.remove(2)
# # a.clear()
#
# a.sort()
# a.reverse()
# a.reverse()
#
#
# print(a)
#
# t = (1, 2, 3,3,2,3,2,4,5,2)
# t2 = tuple([1, 2, 3])
#
# # s = t.index(2)
# s = t.count(2)
# s = t.__add__(t2)
#
#
# # print(type(t))
# # print(type(t2))
# print(s)
#
# a = {"name": "joel", "age": 18}
# b = dict(name="joe", age=18)
#
# a["name"] = "baili"
# a["aihao"] = "dushu"
#
# del a["age"]
#
# a.update(age = 88)
# a.pop("aihao")
#
#
#
#
# print(a)
# print(b)

# print(hash([888]))
#
# print(input("请输入内容：")*3,end='\n')


# a = "abbaccaagasdaadsadddd"
#
# d = {}
# for i in a:
#     d[i] = d.get(i,0) + 1
#
# print(d)

# name = input("请输入你的名字：")
# print(1)
# print("北凡")
# if None:
# # if True:
# if name == "baili":
#     print("baili")
#     print("joel")
#
# elif name == "banfan":
#     print("banfan")
#
# else:
#     print("666")


# a = True
# while a:
#     print("joel")
#     a = False
# print("end")


#
# a = [1, 2, 3, 4, 5, 6, 66, 66, 7, 8]
#
# for i in a:
#     print(i)'

#
# max = 5
# count = 0
# for i in a:
#     print(i)
#     count += 1
#     if count == 3:
#         break
#         print("end")

# for i in a:
#     print(i)
#     for x in range(10):                     # 循环内部，也可以有循环
#         print(x)                                      # 打印数字
#         # continue                                    # 快进到下一次循环 ，快进了哪个循环？
#     print("-" * 20)

# for i in range(1, 10):
#     # print(i)
#     for j in range(1, i + 1):
#         print(f"{i}*{j}={i * j}",end="\t")
#     print()


# row = int(input("请输入您的数字："))
# for i in range(1, row, 2):
#     print(" " * int((row - i) / 2) + '*' * i)

# def print_1():
#     row, line = 4, 0  # 总行数,#换行数
#     while line < row:
#         line += 1
#         print(" " * (row - line), "*" * (1 + (2 * (line - 1))))
#
# print_1()


# # row = int(input("请输入您的数字："))
# x = 20
# for i in range(1, x, 2):
#     print(f"{i * '*'  : ^{x}}")


# a = "abbaccadd"
# s = set(a)
# for i in s:
#     print(i)


# """
# 1.
# 编写函数f_1，使其可以根据输入的参数，返回指定数量的
# '*'
#
# ```
# f_1(1)
# 返回 *
# f_1(3)
# 返回 ** *
# ```
# """
# # i = int(input("请输入："))
#
# c = 1
#
#
# def f_1(c):
#     c += 1
#     print("*" * c)
#
# f1 = f_1(5)
# print(f1)
# """
# 2._
# 编写函数f_2, 可以根据参数决定调用f_1的次数，默认为1次
# -
# ```
# f_2(): 返回 *
# f_2(3): 调用f_1
# 3
# 次
# 返回 ** * ** * ** *
# ```
# """

# def f_2(self): # 这里的括号，表示函数的调用方式
#     f_1(c)
#
# f_2(c)
#
# import copy

# def fib(n, l=None): # 使用默认值的是，不是新建一个默认值，而是使用第一个数据
# # l = [0, 1]
#     l = copy.copy(l) # 在函数中让l 变成预期的样子
#     print(id(l), l)
#     for i in range(n):
#         l.append(l[i] + l[i + 1])
#     print(l) # 生成 前两项是0 和1 的斐波那契数列的后8项
# l = [1, 1]
# fib(2, l, ) # [1,1 ,+2 项] 正确的
# fib(2, l, ) # [1,1 ,+2 项] 正确的
# fib(2, l, ) # [1,1 ,+2 项] 正确的

# l = [1, 2, 3, 4, ]
# # 让函数的参数数量，动态发生变化？
# def append(*args, **kwargs, ):
#     print(type(args), args) # 位置参数，通过元组进行存储
#     print(type(kwargs), kwargs) # 关键字参数，通过字典进行存储
# append(5, 1, 3, 4, 45, 5) # 传递位置参数
# print('-' * 10)
# append(a=1, b=2, c=3) # 传递关键字参数
# print('-' * 10)
# append(5, 1, 3, a=1, b=2, c=3) # 同时传递 位置参数 和关键字参数位置之前，关键字在后

# 1. 创建名为f1的函数，不接收任何参数，返回None
# def f1():
#     pass
# f1()
#
# # 2. 创建名为f2的函数，接收2个整数参数，返回他们相加结果
# def f2(a: int, b: int) -> int:
#     return a + b
#
# f2 = f2(2, 6)
# print(f2)
#
#
# # 3. 创建名为f3的函数，接收任意个参数， 返回他们相加的结果
# def f3(*args):
#     r = None
#     for arg in args:
#         if r is None:
#             r = arg
#         else:
#             r = r + arg
#     return r
#
#
# f3 = f3("2", "5", "6")
# print(f3)


# 4. 创建名为f4的函数，接收一个必填参数，用来标记加法还是减法，再接收任意个参数，
# # 1. 返回他们相加（或相减）的结果
#

# def f4(v, *args):
#     r = None
#     if v == "+":
#         for arg in args:
#             if r is None:
#                 r = arg
#             else:
#                 r = r + arg
#     elif v == "-":
#         for arg in args:
#             if r is None:
#                 r = arg
#             else:
#                 r = r - arg
#
#     return r
#
#
# f4 = f4("-", 5, 9, 6, 3)
# print(f4)

# #
# # # 5. 创建名为f5的函数，接收一个函数，并返回一个函数
# def f5(a):
#     return a
#
# f5 = f5(print)
# print(f5)


"""
创建名为call函数，它接收一个函数f，并接收任意数量、任意类型的参数
调用后 返回值 函数f在收到同样参数的调用结果
1. 定义函数 call
2. 定义函数的参数： f ， 不定长参数
3. 调用函数 call
4. 返回 f的调用结果
"""


#
# def call(f, *args, **kwargs):
#     return f(*args, **kwargs)
#
#
# call = call(print, "5",)
# print()


#
# def f(*args, **kwargs):
#     print(1222)
# f()
#
# def call(f, *args, **kwargs):
#     return f(*args, **kwargs)
#
#     def f(*args, **kwargs):
#         print(1222)
#
#
# call(print,5,6,9)


# 通过类 设计一种动物，他们应该用于不同的名字、体重、身高，每个动物都可以计算出自己的BMI
# class Animal:
#     name = " "
#     weight = 0
#     height = 0
#
#     def bmi(self):
#         bmi = float(self.weight) / float(self.height * 2)
#         return bmi
#
#
# a1 = Animal()
# a2 = Animal()
# a3 = Animal()
#
# a1.name = "a1"
# a1.weight = 100
# a1.height = 160
#
# a2.name = "a2"
# a2.weight = 180
# a2.height = 160
#
# a3.name = "a3"
# a3.weight = 150
# a3.height = 180
#
# print(f"{a1.name}的BMI是{a1.bmi()}")
# print(f"{a2.name}的BMI是{a2.bmi()}")
# print(f"{a3.name}的BMI是{a3.bmi()}")
