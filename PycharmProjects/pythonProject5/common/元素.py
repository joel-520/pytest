"""
1.学习目标:
    必须掌握selenium中元素的输入,点击,清空
2.语法
    2.1 点击
        元素.click()
    2.2 输入
        元素.send_keys(输入的内容)
    2.3 清空
        元素.clear()
    2.4 提交
        元素.submit()
3.需求
    在页面中,完成元素的输入,点击,清空,提交
4.总结
    在对输入框进行输入操作时,先清空再输入（要记住）
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep
import os

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./1.html")
driver.get(url)

# 4.对账号A输入框做输入和清空操作,点击新浪网站连接
# 4.1 定位输入框和百度超链接
# 定位账号A输入框
textA = driver.find_element_by_id("userA")
# 定位百度超链接
baidu = driver.find_element_by_link_text("访问 百度 网站")

# 4.2 输入文字,清空
# 在账号A中输入Selenium
textA.send_keys("Selenium")
sleep(2)
# 清空账号A中的输入内容
textA.clear()
sleep(2)

# 4.3 点击百度超链接
baidu.click()

# 4.4 定位百度输入框
baidu_element = driver.find_element_by_id("kw")

# 4.5 在输入框中输入【心善渊&Selenium基础】
baidu_element.send_keys("【心善渊&Selenium基础】")
sleep(5)
# 4.6 定位按钮 百度一下
yixia_element = driver.find_element_by_id("su")

# 4.7 点击百度一下
"""
submit()调用提交,
submit()的作用等同于click(),
但是click()的使用面要更广一些。
"""
yixia_element.submit()


# 5.关闭浏览器
sleep(2)
driver.quit()