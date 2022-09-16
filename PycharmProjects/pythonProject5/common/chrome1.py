"""
1.学习目标
    熟悉selenium屏蔽谷歌浏览器的信息提示栏
2.操作步骤
    1.导包
    2.添加谷歌浏览器加载项
        屏蔽信息提示栏
    3.打开谷歌浏览器——将屏蔽信息提示栏参数传入到打开浏览器中
    4.打开地址
    5.关闭浏览器

    总结：
    options = webdriver.ChromeOptions()  # 实例化谷歌浏览器加载项
    options.add_argument("disable-infobars")  # 去掉谷歌浏览器信息提示栏
    webdriver.Chrome(chrom_options=options)  # 使用浏览器加载项
3.需求
    使用selenium将谷歌浏览器的信息提示栏屏蔽
"""
# 1.导入selenium包
from selenium import webdriver
from time import sleep

# 2.添加谷歌浏览器加载项
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")

# 3.打开谷歌浏览器——将屏蔽信息提示栏参数传入打开浏览器中
"""
DeprecationWarning: use options instead of chrome_options
弃用警告：使用选项代替chrome_options,改用options选项
"""
driver = webdriver.Chrome(options=options)

# 4.打开地址
url = "http://www.baidu.com"
driver.get(url)
sleep(3)

# 5.关闭浏览器
driver.quit()