# 方法一：条件判断和2取余数为0则累加计算
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1

# 输出2550
print(result)


# 方法二：计数器控制增量为2
i = 0
result = 0
while i <= 100:
    result += i
    i += 2

# 输出2550
print(result)