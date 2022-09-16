
# 要说的话  word s ="希望大家都能被爱的人温柔以待,：虽然不能与你感同身受,但可以做你但最佳听众"

import pyautogui
# 控制键盘鼠标
import pyperclip
# 控制电脑的复制截切版
import time

# 控制时间
time.sleep(5)
# 设置切换窗口时准备的时间
for i in words.split("/n" ) *99:
    # split("/n")把文章分成一句一句的
    print(i)
    pyautogui.click(477 ,703)
    # 提取坐标，通俗一点就是鼠标点一下这个位置,定位聊天窗口
    pyperclip.copy(i)
    # 复制到截切版上去
    pyautogui.hotkey("ctrl" ,"v")
    # 粘贴
    pyautogui.typewrite("\n")
    # 回车
    time.sleep(0.5)
    # 让语速不太快
