"""
1.学习目标
    熟悉selenium使用谷歌浏览器模拟移动端
2.操作步骤
    1.导包
    2.添加谷歌浏览器加载项
        设置模拟的手机型号，字典类型的参数
        mobileEmulation = {"deviceName": "iPhone X"}
        options=webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobileEmulation)
        注："mobileEmulation"为固定写法。
    3.打开谷歌浏览器——将参数传入打开的浏览器中
    4.打开地址
    5.关闭浏览器
3.需求
    使用selenium打开谷歌浏览器，模拟iPhoneX手机

"""
# 1.导入selenium包
from selenium import webdriver
from time import sleep

# 2.添加谷歌浏览器加载项
mobileEmulation = {"deviceName": "iPhone X"}
options = webdriver.ChromeOptions()
# 因为传入的是字典类型的数据，所以使用的add方法也不一样
options.add_experimental_option("mobileEmulation", mobileEmulation)

# 3.打开谷歌浏览器——将模拟移动端的参数，传入打开的浏览器中
# options和chrome_options一样，chrome_options将弃用。
driver = webdriver.Chrome(options = options)

# 4.打开地址
url = "http://www.baidu.com"
driver.get(url)
sleep(3)

# 5.关闭浏览器
driver.quit()
