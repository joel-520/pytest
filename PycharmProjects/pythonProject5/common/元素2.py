"""
1.学习目标:
    掌握selenium中元素的其他操作
2.语法
    2.1 size 获取元素大小
        元素.size
    2.2 text 获取元素文本（掌握）
        元素.text  2个标签之间的文字
    2.3 get_attribute() 获取元素属性（掌握）
        元素.get_attribute("属性名")
    2.4 is_displayed() 判断元素是否可见（掌握）
        元素.is_displayed()
    2.5 is_enabled()  判断元素是否可用（掌握）
        元素.is_enabled()
    2.6 获取页面标题
        driver.title
    2.7 获取当前页面url
        driver.current_url
3.需求
    在页面中,完成上面操作。
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep
import os

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./2.html")
driver.get(url)

# 4.元素其他操作---按钮
button = driver.find_element_by_css_selector("button[type='submitA']")

# 4.1 获取元素大小
print("元素大小:", button.size)

# 4.2 获取元素文本
print("元素文本:", button.text)

# 4.3 获取元素属性
print("元素的value属性值:", button.get_attribute("value"))
print("元素的title属性值:", button.get_attribute("title"))
# 没有的属性为空，什么都不打印，但不报错
print(button.get_attribute("id"))

# 4.4 判断元素是否可见
print("button按钮是否可见:", button.is_displayed())

# 4.5 判断元素是否可用
print("button按钮是否可用:", button.is_enabled())

# 4.6 获取页面标题
print("页面的title：", driver.title)

# 4.7 获取当前页面url
print(driver.current_url)

# 5.关闭浏览器
sleep(2)
driver.quit()
"""
输出结果：
元素大小: {'height': 23, 'width': 78}
元素文本: 注册用户A
元素的value属性值: 注册A
元素的title属性值: 加入会员A

button按钮是否可见: True
button按钮是否可用: True
页面的title： 注册A
file:///J:/PyCharmWorkSpace/firstproject/selenium/demo/2.html
"""