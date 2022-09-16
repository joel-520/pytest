# 1.导入selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./1.html")
driver.get(url)
sleep(2)

# 4.定位目标元素
# 4.1 通过id属性定位页面中账号A输入框
# 写法一
element_id_1 = driver.find_element(By.ID, "userA")
print(element_id_1.get_attribute("outerHTML"))
# 写法二
element_id_2 = driver.find_element("id", "userA")
print(element_id_2.get_attribute("outerHTML"))

# 4.2 通过name属性定位页面中账号A输入框
# 写法一
element_name_1 = driver.find_element(By.NAME, "userA")
print(element_name_1.get_attribute("outerHTML"))
# 写法二
element_name_2 = driver.find_element("name", "userA")
print(element_name_2.get_attribute("outerHTML"))

# 4.3 通过class属性定位页面中账号A输入框
# 写法一
element_class_1 = driver.find_element(By.CLASS_NAME, "c_uA")
print(element_class_1.get_attribute("outerHTML"))
# 写法二
element_class_2 = driver.find_element("class name", "c_uA")
print(element_class_2.get_attribute("outerHTML"))

# 4.4 通过tag_name定位页面中账号A输入框
# 写法一
element_tag_name_1 = driver.find_element(By.TAG_NAME, "input")
print(element_tag_name_1.get_attribute("outerHTML"))
# 写法二
element_tag_name_2 = driver.find_element("tag name", "input")
print(element_tag_name_2.get_attribute("outerHTML"))

# 4.5 通过link_text定位页面中超链接
# 写法一
element_link_text_1 = driver.find_element(By.LINK_TEXT, "访问 新浪 网站")
print(element_link_text_1.get_attribute("outerHTML"))
# 写法二
element_link_text_2 = driver.find_element("link text", "访问 新浪 网站")
print(element_link_text_2.get_attribute("outerHTML"))

# 4.6 通过partial_link_text定位页面中超链接
# 写法一
element_partial_link_text_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "问 新浪")
print(element_partial_link_text_1.get_attribute("outerHTML"))
# 写法二
element_partial_link_text_2 = driver.find_element("partial link text", "问 新浪")
print(element_partial_link_text_2.get_attribute("outerHTML"))

# 4.7 通过XPath定位页面中账号A输入框
# 写法一
element_xpath_1 = driver.find_element(By.XPATH, "//input[@id='userA']")
print(element_xpath_1.get_attribute("outerHTML"))
# 写法二
element_xpath_1 = driver.find_element("xpath", "//input[@id='userA']")
print(element_xpath_1.get_attribute("outerHTML"))

# 4.8 通过css_selector定位页面中账号A输入框
# 写法一
element_css_selector_1 = driver.find_element(By.CSS_SELECTOR, "input#userA")
print(element_css_selector_1.get_attribute("outerHTML"))
# 写法二
element_css_selector_2 = driver.find_element("css selector", ".c_uA")
print(element_css_selector_2.get_attribute("outerHTML"))

# 5.关闭浏览器
driver.quit()

"""
输出结果：
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<a href="http://www.sina.com.cn" id="fwA">访问 新浪 网站</a>
<a href="http://www.sina.com.cn" id="fwA">访问 新浪 网站</a>
<a href="http://www.sina.com.cn" id="fwA">访问 新浪 网站</a>
<a href="http://www.sina.com.cn" id="fwA">访问 新浪 网站</a>
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
<input type="textA" name="userA" id="userA" class="c_uA" placeholder="账号A" required="" value="">
"""
