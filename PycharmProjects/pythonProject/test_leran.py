# -*- coding: utf-8 -*-
# @Time : 2022/7/25 9:27
# @Author : joel
# @Email : 770546904@qq.com
# @File : test_leran.py

#
# a = [1, 2, 3]  # 直接创建列表
# b = list("abcde")  # 通过其他数据转为列表
# print(a)
# print(b)

# a = []
# a.append(1) # 把一个数据加入到列表
# a.append(1) # 把一个数据加入到列表
# a.extend([2, 3, 4]) # 把一组数据，加入列表
# a.insert(0, "beifan") # 把一个数据，放入到指定的位置
# # 列表的底层结构，决定了 在右侧读写，效率更高
# print("添加内容", a)
# a.pop() # 把最右侧的数据，移除\
# print("删除1个内容", a)
# a.remove("beifan") # 移除指定数据
# print("删除beifan", a)
# a.pop(0) # 移除指定下标的数
# print("删除第一个数字", a)
# a.clear() # 移除全部的数据
# print("移除全部的数据",a )


# a = (1, 2, 3) # 直接创建元组
# b = tuple([3, 2, 1]) # 同列表转为元组
# print(a)
# print(b)
# # print(a[::-1])
# print(a[1])


# a = {
# "name": "北凡",
# "age": 18,
# }
# # 底层原理，根据key找到value
# a["name"] = "百里" # 将key是name的数据，改为 百里，实现添加和修改数据
# print("修改数据", a)
# a["tel"] = "13191121211"
# print("添加数据", a)
# del a['age']
# print("删除数据", a)

# a = "abbaccadd"
# d = {}
# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] =1
# l = sorted(d.items(),key=lambda x:x[1],reverse=True)
# print(l)
#

