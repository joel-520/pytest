import win32gui
import win32api
import win32con
import time
import random

import win32clipboard as w


def getClipBoardText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


def setClipBoardText(data):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(data)
    w.CloseClipboard()


def ctrlV():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def altS():
    win32api.keybd_event(18, 0, 0, 0)  # Alt键位码
    win32api.keybd_event(83, 0, 0, 0)  # s键位码
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)


weixin = win32gui.FindWindow(None, "微信")
win32gui.SetForegroundWindow(weixin)
left, top, right, bottom = win32gui.GetWindowRect(weixin)
print(left, top, right, bottom)

theWordYouWantToSay = ("hahhahhahhahhahahahhhahahahahahhhhhahhhahhhahahahahha", "hhahahhahhahahahahhaha")

for i in range(0, 50):
    click_x = 732 - 423 + left + 80  # 亲测不管怎么改变微信窗口打下,click_x 和clilck_y总能点到输入框
    click_y = bottom - (918 - 775) + 60

    win32api.SetCursorPos([click_x, click_y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    setClipBoardText(theWordYouWantToSay[random.randint(0, len(theWordYouWantToSay) - 1)])
    ctrlV()
    # 发送回车
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.3)
