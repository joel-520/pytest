"""
1.学习目标:
    掌握单选框操作
2.语法
    1.定位单选框,进行点击操作
        再进行一下点击操作，就是取消选择
    2.在点击之前,需要判断单选框是否被选中
        元素.is_selected()  # 判断元素是否被选中
3.需求
    在页面中,操作单选框
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
sleep(2)

# 4.单选框操作
# 4.1 定位单选框
# 定位选项前的按钮元素，不要定位文字
apple = driver.find_element_by_id("pg")

# 4.2 操作单选框
# 判断单选框是否被选中
if apple.is_selected():
    pass
else:
    # 单击一下，让单选按钮进入选中状态
    apple.click()
    sleep(2)

"""
注意：
被禁用的按钮是不能被操作的，
也就是按钮属性中有disabled=""。
单选按钮和多选按钮都是。
"""

# 5. 操作一组单选框
# 5.1定位所有的单选框
radios = driver.find_elements_by_css_selector("input[type='radio']")

# 5.2 遍历操作所有的单选框
for radio in radios:
    if radio.is_selected():
        pass
    else:
        radio.click()
        sleep(1)

# 5.关闭浏览器
driver.quit()


# 1.导入selenium
from selenium import webdriver
from time import sleep
import os

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "file:///" + os.path.abspath("./1.html")
driver.get(url)
sleep(2)

# 4. 选择部分多选框
# 建立列表填写将要选择的复选框名称
box_list = ["购物", "旅游"]

# 定位所有的复选框
checkboxes = driver.find_elements_by_name("checkbox")

# 遍历选择
for checkbox in checkboxes:
    # 判断获取到的复选框的名称和在需求勾选的复选框中
    if checkbox.get_attribute("value") in box_list:
        # 如果在，判断选框是否被选中
        if checkbox.is_selected():
            pass
        else:
            # 单击一下，让单选按钮进入选中状态
            checkbox.click()
            sleep(1)

"""
注意：
被禁用的按钮是不能被操作的，
也就是按钮属性中有disabled=""。
单选按钮和多选按钮都是。
"""

# 5.关闭浏览器
driver.quit()




"""
1.学习目标:
    必须掌握web中多窗口切换方法
2.语法(操作步骤)
    2.1 获取当前窗口句柄
        driver.current_window_handle
    2.2 点击页面中的超链接触发多窗口
    2.3 获取所有窗口句柄
        driver.window_handles
    2.4 进入新窗口
        switch_to.window(handles[1])
    2.5 操作新窗口中的元素
        按实际工作需求编写
    2.6 退出新窗口
        switch_to.window(handles[0])

3.需求
    在页面中,实现多窗口切换。
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开我的Python文档页面
url = "https://blog.csdn.net/Liuyuelinjiayou/article/details/105789238"
driver.get(url)
sleep(2)

# 4. 多窗口切换操作
# 4.1 获取当前窗口句柄
handle = driver.current_window_handle
print('点击之前的窗口句柄是:', handle)
print('点击前的url:', driver.current_url)

# 4.2 点击页面中的超链接触发多窗口
driver.find_element_by_link_text("PyCharm下载与安装").click()
sleep(2)

# 4.2 获取所有窗口句柄
handles = driver.window_handles

# 4.3 进入新窗口
driver.switch_to.window(handles[1])
print('点击之后浏览器所有的窗口句柄是:', handles)
print('点击后的url:', driver.current_url)

# 4.5 退出新窗口
# 你需要退到哪个窗口就写哪个窗口的handle索引
# 因为handle在上边赋值等于第一个窗口了，这里就可以写handle
# 也可以写handles[0]
driver.switch_to.window(handle)
sleep(10)

# 5.关闭浏览器
driver.quit()

"""
输出结果：
点击之前的窗口句柄是: CDwindow-6F1E6437F354913663E6A7E5A1486784
点击前的url: https://blog.csdn.net/Liuyuelinjiayou/article/details/105789238

点击之后浏览器所有的窗口句柄是: ['CDwindow-6F1E6437F354913663E6A7E5A1486784', 'CDwindow-48640D53F053821ED38D21B87E549A73']
点击后的url: https://blog.csdn.net/Liuyuelinjiayou/article/details/105729957
"""


"""
1.学习目标:
    必须掌握iframe表单操作方式
2.语法(操作步骤)
    2.1 确定即将操作的元素是否属于iframe
        F12中elements最下方查看是否有iframe/frame标签名
    2.2 定位iframe/frame标签
    2.3 进入iframe
        driver.switch_to.frame(参数)
        参数:
            当iframe标签有id/name属性时,参数=id/name的属性值,无需定位。
                driver.find_element_by_id("idframe")
            当iframe标签没有id/name属性时,先定位,参数=定位元素
                el_frame = driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]")
                driver.switch_to.frame(el_frame)
            当明确页面中iframe索引值,参数=索引值
                driver.switch_to.frame(0)  # 参数=索引值  从0开始
                (也就是页面中有几个iframe，和你需要的iframe的索引，你都知道就可以用)
    2.4 操作iframe中的元素
        和普通页面一样
    2.5 退出iframe
        退出到上一层   driver.switch_to.parent_frame()
        退出到最外层 driver.switch_to.default_content()
        具体跳出到哪一层,根据下一步操作而定。
3.需求
    在163邮箱登陆页面中，操作iframe元素。
4.iframe在web中的应用位置
    1.一般的登录,163邮箱,qq邮箱,
    2.发邮件(富文本编辑器一般是嵌入到页面中的，也就是邮件的正文也是iframe),
    3.后台管理菜单栏
"""
# 1.导入selenium
from selenium import webdriver
from time import sleep

# 2.打开浏览器
driver = webdriver.Chrome()

# 3.打开页面
url = "https://mail.163.com/"
driver.get(url)
sleep(2)

# 4.iframe操作
# 4.1 进入iframe表单
# 4.1.1 方式一：先定位iframe表单再进入
el_frame = driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]")
# print(el_frame.get_attribute("outerHTML"))
# 4.1.2 切换进入表单中
driver.switch_to.frame(el_frame)

# 4.1.3 方式二：直接通过id或name进入表单中
# 如下id不正确
# driver.switch_to.frame('x-URS-iframe')

# 4.1.4 方式三：通过索引值切换进入表单
# 参数=索引值  从0开始
# driver.switch_to.frame(0)  # 可用

# 4.2 操作表单中的元素
# 4.2.1 定位账号输入框和密码输入框
email = driver.find_element_by_css_selector("input[name='email']")
password = driver.find_element_by_css_selector("input[name='password']")
sleep(2)

# 4.2.2 填写内容
email.clear()
email.send_keys("Selenium")
password.clear()
password.send_keys("Selenium")
sleep(2)

# 4.3 跳出页面中表单
# 因为页面中只有一层iframe，所以跳到上一层和最外层一样效果。
# 4.3.1 跳到最外层
driver.switch_to.default_content()

# 4.3.2 跳到上一层
# driver.switch_to.default_content()
sleep(2)

# 4.4 点击网易首页
driver.find_element_by_link_text("网易首页").click()
sleep(3)

# 5.关闭浏览器
driver.quit()