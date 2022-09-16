"""
1.学习目标
    掌握selenium中控制浏览器窗口大小的方法
2.操作步骤（方法）
    2.1设置浏览器窗口大小，宽度，高度
        driver.set_window_size（宽，高）
    2.2 获取浏览器窗口大小
        driver.get_window_size()
    2.3将浏览器窗口最大化
        driver.maximize_window）
3.需求
    使用selenium实现对浏览器窗口大小的设置
"""
# 1.导入seleniun
from selenium import webdriver
from time import sleep

# 2.打开谷歌浏览器（获取浏览器操作对象）
driver = webdriver.Chrome()

# 3.设置浏览器窗口大小
# 3.1 将窗口设置为宽100，高200
# (windowHandle参数为窗口句柄，以后再说)
driver.set_window_size(100, 200)
sleep(3)

# 3.2 获取浏览器窗口大小
window_size = driver.get_window_size()
print(window_size)

# 3.3 窗口最大化
driver.maximize_window()

# 4.关闭浏览器
driver.quit()
"""
输出结果：
{'width': 516, 'height': 200}
"""


"""
1.学习目标
    掌握selenium中控制浏览器窗口位置的方法
2.操作步骤（方法）
    2.1 设置浏览器窗口位置（横纵坐标）
        set_window_position(横坐标，纵坐标)
    2.2 获取浏览器窗口位置
        driver.get_window_position()

3.需求
    使用selenium实现对浏览器窗口位置的设置
"""
# 1.导入seleniun
from selenium import webdriver
from time import sleep

# 2.打开谷歌浏览器（获取浏览器操作对象）
driver = webdriver.Chrome()

# 3.设置浏览器位置
# 3.1 将窗口的位置设置为100，300
driver.set_window_position(100, 300)
sleep(2)

# 3.2 获取浏览器窗口位置
window_position = driver.get_window_position()
print(window_position)

# 4.关闭浏览器
driver.quit()

"""
输出结果：
{'x': 100, 'y': 300}
"""

"""
1.学习目标
    掌握selenium控制浏览器的前进，后退，刷新
2.操作步骤（语法）
    2.1前进
        driver.forward（）
    2.2后退
        driver.back（）
    2.3刷新
        driver.refresh（）
3.需求
    使用谷歌浏览器分别打开百度，京东，淘宝，使用前进，后退，刷新方法
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep

# 2.打开浏览器---谷歌浏览器
driver = webdriver.Chrome()
# 3.窗口最大化
driver.maximize_window()
sleep(2)
# 4.输入网址百度，京东，淘宝
driver.get("http://www.baidu.com")
sleep(2)
driver.get("http://www.jd.com")
sleep(2)
driver.get("http://www.taobao.com")
sleep(2)
# 5.使用前进，后退，刷新命令
# 前进
driver.back()  # 后退到京东
sleep(2)
driver.back()  # 后退到百度
sleep(2)
# 后退
driver.forward()  # 前进到京东
sleep(2)
driver.forward()  # 前进到淘宝
sleep(2)

# 刷新
driver.refresh()  # 保持在淘宝页面
sleep(2)

# 6.关闭浏览器，同时关闭浏览器驱动
driver.quit()

# 只关闭当前浏览器窗口
driver.close()