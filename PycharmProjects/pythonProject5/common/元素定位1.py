"""
学习目标
    复数形式
        复数定位形式:driver.find_elements_XXX
        复数定位,返回的列表类型数据<list>
        遍历列表操作具体元素
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep

# 2.打开浏览器
driver = webdriver.Chrome()
# 3.输入网址
url = "http://www.baidu.com"
driver.get(url)
sleep(2)

# 4.通过by_id复数定位
srk = driver.find_elements_by_id("kw")
# 5.查看返回结果数据类型
print("结果数据类型", type(srk))
print("元素个数", len(srk))

# 6.遍历结果，查看源码
for i in srk:
    # 查看元素对应的源码
    print(i.get_attribute("outerHTML"))

# 7.关团浏览器
driver.quit()

"""
结果数据类型 <class 'list'>
元素个数 1
<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
"""