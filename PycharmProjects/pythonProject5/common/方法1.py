# 两种导入都可以
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

"""
1.学习目标:
    必须掌握鼠标悬停、按下的操作方法
2.语法
    2.1 导入ActionChains
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver import ActionChains
    2.2 使用方法
    ActionChains(driver).鼠标事件(需要鼠标操作的元素).perform()
    2.3 鼠标悬停
        move_to_element(需要操作的元素)
    2.4 鼠标按下
        click_and_hold(需要操作的元素)
3.需求
    在页面中,完成上述操作。
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver import ActionChains

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./4.html")
driver.get(url)
sleep(2)

# 4.对注册按钮,执行鼠标悬停、按下事件
# 4.1 鼠标悬停-按钮变黄
# 4.1.1 定位注册按钮
button = driver.find_element_by_css_selector("button[type='submitA']")

# 4.1.2 执行鼠标悬停事件
ActionChains(driver).move_to_element(button).perform()
sleep(3)

# 4.2 鼠标按下，按钮变红
# 4.2.1 执行鼠标按下事件
ActionChains(driver).click_and_hold(button).perform()
sleep(3)

# 5.关闭浏览器
driver.quit()




"""
1.学习目标:
    掌握selenium中键盘事件的操作
2.语法
    2.1 导入Keys类
    from selenium.webdriver.common.keys import Keys
    2.2 使用
    元素.send_keys(键名称)
        1.单个键使用
            (Keys.键名称)
            注意：键名称全大写字母
        2.组合键
            (Keys.键名称,"c")

3.需求
    在页面中,完成文字内容的复制操作。
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.keys import Keys

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./1.html")
driver.get(url)

# 4.键盘事件
# 在账号A中输入"Selenium",将输入的内容复制到密码A输入框中
# 4.1 定位账号A和电话A
textA = driver.find_element_by_id("userA")  # 账号A
passwordA = driver.find_element_by_id("passwordA")  # 密码A

# 4.2 在账号A中输入"Selenium"
textA.clear()
textA.send_keys("Seleniumm")
sleep(2)

# 4.3 使用退格键删除m字母
textA.send_keys(Keys.BACKSPACE)
sleep(2)

# 4.4 将账号A中的文字复制
# 全选账号A中的文字
textA.send_keys(Keys.CONTROL, "a")
# 复制账号A中的文字
textA.send_keys(Keys.CONTROL, "c")

# 4.5 将复制的内容粘贴到密码A输入框中
passwordA.send_keys(Keys.CONTROL, "v")

# 5.关闭浏览器
sleep(2)
driver.quit()




"""
1.学习目标:
    掌握selenium中Select类使用
2.语法(操作步骤)
    2.1导入Select类
    2.2 定位下拉框的select标签
    2.3 使用Select类提供的方法选择选项
        2.3.1 通过选项的value值选择
            select_by_value("value属性值")
        2.3.2 通过选项索引值选择 索引从0开始
            select_by_index(索引值)
        2.3.3 通过选项名称选择
            select_by_visible_text(选择名称)
3.需求
    在页面中,使用Select类操作下拉框
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.select import Select

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./3.html")
driver.get(url)
sleep(2)
# 4.使用Select类操作下拉框
# 4.1 定位下拉框标签
selectA = driver.find_element_by_id("selectA")

# 4.2 通过Select类选择选项
# 创建下拉框对象
# Select(定位下拉框的元素--select标签元素)
select = Select(selectA)

# 通过value值选择选项（选择上海）
select.select_by_value("sh")
sleep(2)

# 通过index值选择选项，索引从0开始（选择广州）
select.select_by_index(2)
sleep(2)

# 通过text值选择选项（选择北京）
select.select_by_visible_text("A北京")
sleep(2)

# 5.关闭浏览器
driver.quit()
