# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
if __name__ == '__main__':
# 初始化一个webdriver实例
 wd = webdriver.Chrome()
# 访问百度
 wd.get("http://www.baidu.com")
# 等待5s
sleep(5)
# 关闭浏览器
wd.close()


