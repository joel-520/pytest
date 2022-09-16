import random  #导入模块
# ↓↓↓ 定义初始变量
a =0  # 用来记录人物A掷投掷的结果
b =0  # 用来记录人物B掷投掷的结果
level_score =0  # 用来记录双方平局次数
score_A =0  # 人物A的每小局胜利次数
score_B =0  # 人物B的每小局胜利次数

for x in range(50):  # 进行50盘比赛
    for n in range(5):  # 模拟双方每盘摇5次骰子
        person_A =random.randint(1,6)  # 使用random模块的randit进行1~6模拟摇骰子的过程
        a +=person_A  # 将投掷结果保存

        person_B =random.randint(1,6)# 使用random模块的randit进行1~6模拟摇骰子的过程
        b +=person_B  # 将投掷结果保存
    if a>b:  # 比较5局以后双方投掷结果总和，将比较结果保存至本场比赛最终结果
        score_A+=1 # A本盘获胜
    elif a<b: # B本盘获胜
        score_B+=1
    else:
        level_score+=1
    a =0  # 重置双方分数，并进入下一轮循环
    b =0  # 重置双方分数，并进入下一轮循环
    # 此处如果不重置分数，本次投掷结果将会进入下一次循环，有悖题目要求和比赛公平性。
if score_A>score_B:  # 比较最终结果，游戏结束
    print(f'本次比赛A胜，A总分为：{score_A}，B总分为：{score_B},比赛期间平局次数为：{level_score}')
elif score_A<score_B:
    print(f'本次比赛B胜,A总分为：{score_A},B总分为：{score_B},比赛期间平局次数为：{level_score}')
else:
    print(f'本次比赛平局，双方总分：A{score_A} vs B{score_B},比赛期间平局次数为：{level_score}')
