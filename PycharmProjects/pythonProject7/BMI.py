#
# """1.用input输入一个人的身高和体重，并根据BMI公式（体重/身高的平方）计算出BMI的指数，并判断BMI等级
# 判断规则
# BMI<18.5:过轻
# BMI 18.5~23.9 正常
# BMI 24~27.9 超重
# BMI 28~32 肥胖
# BMI>32 严重肥胖
# """
height = float(input("请输入您的身高（M）:"))
weight = float(input("请输入您的体重(KG):"))
BMI = float(float(weight)/float(height**2))
if BMI <18.5:
    print("过轻")
elif BMI >=18.5 and BMI < 23.9:
    print("正常")
elif BMI >= 23.9 and BMI < 27.9:
    print("超重")
elif BMI >= 27.9 and BMI < 32 :
    print("肥胖")
else:
    print("严重肥胖")
#
# # 2.定义一个变量判断是否有票，如果有票，则进行安检，判断刀的长度是否大于20，大于20提示：刀的长度超过20，不准通过，未超过则允许通过，如果没票则提示，请先购票！
# is_ticket = input("请输入是否有票:")
# if is_ticket == 'true':
#     knife = float(input("请输入刀的长度:"))
#     if knife > 20 :
#         print("不准通过！")
#     elif knife > 0 and knife <= 20:
#         print("允许通过")
#     else:
#         print("请输入大于0的值")
# elif is_ticket == 'false':
#     print("请先购票")
# else:
#     print("请输入true或者false")
#
# # 3.定义一个天气变量获取用户输入数值（1为晴天，2为雨天），判断天气，如果天气是晴天就出门逛商场，在判断商场里是否还有冰淇淋（1为有），有就打印可以吃冰淇淋，没有就打印商场冰淇淋卖没了，没有冰淇淋吃，如果天气是雨天就打印下雨天不打算出门
# weather = input("请输入今天的天气:")
# if weather == '1':
#     ice = input("是否有冰淇淋：")
#     if ice == '1':
#         print("可以吃冰淇淋")
#     else:
#         print("冰淇淋卖没了")
# else:
#     print("下雨天，不打算出门！")
#
# # 4.输入一个数字，判断是否能被3整除，如果可以，判断是否能被5整除，如果可以则打印“数字*既能被3整除又能被5整除”，如果不可以，则打印“数字*只能被3整除”或“数字*只能被5整除”
# num = int(input("请输入您的值:"))
# if num %3 == 0 and num % 5 ==0 :
#     print("既能被3整除，也能被5整除")
# elif num %3 == 0 and num % 5 !=0:
#     print("值能被3整除")
# elif num %3 != 0 and num % 5 ==0:
#     print("值能被5整除")
# else:
#     print("既不能被3整除，也不能被5整除")
#
# # 5.通过控制台输入三个任意整数，请把这三个整数按从小到大输出
# a = int(input("请输入第一个整数:"))
# b = int(input("请输入第二个整数:"))
# c = int(input("请输入第三个整数:"))
# if a > b :
#     if b > c :
#         print(c,b,a)
#     else:
#         if a > c :
#             print(b,c,a)
#         else:
#             print(b,a,c)
# else:
#     if b < c:
#         print(a,b,c)
#     else:
#         if a < c:
#             print(a,c,b)
#         else:
#             print(c,a,b)
#
#
# # While 循环练习题
# # 1.使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
# a = 0
# while a <12:
#     a += 1
#     if a == 6 or a == 10:
#         continue
#     print(a)
#
# # 2.使用 while 循环实现输出 1-100 内的所有奇数
# a = 1
# while a <100:
#     print(a)
#     a += 2
#
# # 3.用while循环实现用户登录，用户三次输错密码，则提示密码输错三次，请明天再试
# user = 'itcast'
# passwd = '123456'
# a = 0
# while a < 3:
#     username = input("请输入您的用户名:")
#     password = input("请输入您的密码:")
#     if user == username and passwd == password:
#         print("登录成功！")
#         break
#     elif password != passwd and username == user:
#         print("密码错误！")
#     elif username != user:
#         print("用户名错误！")
#     a += 1
#     if a == 3:
#         print("输错三次，请明天再来")
#
# # 4.使用while循环实现猜数字游戏，电脑随机生成一个1-100的数字，用户有5次机会输入，如果输入的数大于电脑随机生成的数字，则给出对应提示，相反，则给出另外提出，如果猜中则给出恭喜您，猜中了！
# import random
# com = random.randint(1,100)
# i = 0
# while i <5:
#     num = int(input("请输入您要猜的数字"))
#     if com > num :
#         print("小了!")
#     elif com < num :
#         print("大了!")
#     else:
#         print("电脑出的数字是:%d"%com)
#         print("恭喜您，猜中了！")
#         break
#     i +=1
#     if i ==5 :
#         print("电脑出的数字是:%d"%com,"很遗憾，下次再来")
#
# #

# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

# num = int(input("输入一个数字: "))
# if (num % 2) == 0:
#     print("{0} 是偶数".format(num))
# else:
#     print("{0} 是奇数".format(num))

# For循环练习
# 1.求 100内偶数之和
# sum = 0
# for i in range(0,100,2):
#     if i % 2 == 0:
#     sum += i
# print(sum)

# 1.求 100内奇数之和
# num = 0
# for i in range(0,100):
#     if i % 2 == 1:
#         num += i
# print(num)

# if 嵌套
# while True:
#     a = int(input())
#     b = int(input())
#
#     if a > b:
#         if a % 2 ==0:
#             print("%s是一个偶数" % a)
#         else:
#             print("%s是一个奇数" % a)
#     else:
#         if b % 2 == 0:
#             print("%s是一个偶数" % a)
#         else:
#             print("%s是一个奇数" % a)
# # 2.使用for循环打印出所有“水仙花数”，所谓水仙花数是指一个三位数，其各位数字立方和等于其本身，例如，153是一个水仙花数，1的立方+5的立方+3的立方等于153。分析：如何对每个数十位、百位、个位进行分解。
# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if a**3 + b**3 + c**3 == i:
#         print("%d是一个水仙花数!"%i)

# # 3.冒泡排序
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i]),