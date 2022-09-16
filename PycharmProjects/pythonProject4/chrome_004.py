

from selenium.webdriver.support.select import Select
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
# 两种导入都可以
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time

#显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 打开谷歌浏览器，获取操作对象
driver = webdriver.Firefox
driver().get("http://10.0.3.243:8088")
#隐式等待
# driver.implicitly_wait(2)
#显示等待
# new = WebDriverWait(driver,30).until(EC.element_to_be_clickable())
# def wait_element(driver,timeout,poll,locator):
# 	#locator=("xpath","//")
# 	used_time=0
# while used_time < timeout
# while True
# 	try:
# 			e=driver.find_element(*locator)
# 			return e
# 		#driver.find_element(By.XPATH,"//input[@id="kw"]")
# 	except:
# 		#time.sleep(0.2)
# 		time.sleep(poll)
# 		used_time+=poll
# #超时了
# raise TimeoutError("元素定位超时")
# wait_element(driver,30,0.4,("id","kw"))


# 设置浏览器窗口大小
# 将窗口设置为宽100，高200
# (windowHandle参数为窗口句柄，以后再说)
# driver.set_window_size(100, 200)
# sleep(3)

# 获取浏览器窗口大小
# window_size = driver.get_window_size()
# print(window_size)

# 窗口最大化(
# driver.maximize_window()

# 定位元素属性,登录
Accout = driver.find_element(by=By.ID, value="phone").send_keys("18117495115")

password = driver.find_element(by=By.NAME,value="password").send_keys("666666")

button = driver.find_element(by=By.ID,value="loginButton").click()



# # 4.输入网址百度，京东，淘宝
# driver.get("http://www.baidu.com")
# sleep(2)
# driver.get("http://www.jd.com")
# sleep(2)
# driver.get("http://www.taobao.com")
# sleep(2)
# # 5.使用前进，后退，刷新命令
# # 前进
# driver.back()  # 后退到京东
# sleep(2)
# driver.back()  # 后退到百度
# sleep(2)
# # 后退
# driver.forward()  # 前进到京东
# sleep(2)
# driver.forward()  # 前进到淘宝
# sleep(2)
#
# # 刷新
# driver.refresh()  # 保持在淘宝页面
# sleep(2)



#点击进入用印申请模块
add1 = driver.find_element(by=By.XPATH,value="//*[text()='用印申请']").click()

#点击进入用印申请
add2 = driver.find_element(by=By.XPATH,value="//a[contains(@url-data,'preList')]").click()

#新增按钮
driver.switch_to.frame("pages_iframe")
add3 = driver.find_element(by=By.XPATH,value="//a[contains(@class,'com_btn com_btn_radius com_btn_small layer')]").click()

# driver.switch_to.default_content()#跳转出来

#新增用印申请页面，跳转iframe
iframe = driver.find_element(by=By.XPATH,value="//div[@class='layui-layer-content']/iframe")
driver.switch_to.frame(iframe)

add4 = driver.find_element(by=By.XPATH,value="//input[contains(@placeholder,'请输入')]").send_keys('test_'+str((random.randint(0o00001, 9999999))))
# sleep(2)
dr = driver.find_element(by=By.XPATH,value="//div[@class='layui-select-title']/input").click()

add5 = driver.find_element(by=By.XPATH,value="//dd[text()='无水印远程']").click()

add6=driver.find_element(by=By.ID,value="selectSealInfoText1").click()


# driver.switch_to.default_content()#跳转出来

#选择印章页面，跳转iframe
find_element = driver.find_element(by=By.XPATH)
iframe = driver.find_element(by=By.XPATH,value="//div[@class='layui-layer-content']/iframe")
driver.switch_to.frame(iframe)
add7=driver.find_element(by=By.XPATH,value="//div[@class='layui-table-cell laytable-cell-1-0-0']").click()

# sleep(1)
# if add7.is_selected():
#     print("pass")

# add8=driver.find_element(By.XPATH,"//a[text()='【智】测试专用章-Joel-243']").click()


# #点击进入印章管理模块
# add1 = driver.find_element(By.XPATH,"//*[text()='印章管理']").click()
# sleep(2)
#
# add2 = driver.find_element(By.XPATH,"//*[text()='印章库']").click()
# sleep(2)

# #新增印章按钮
# driver.switch_to.frame("pages_iframe")
# added4 = driver.find_element(By.XPATH,"//a[contains(@class,'com_btn com_btn_radius com_btn_small layer')]").click()
# sleep(2)
# driver.switch_to.default_content()#跳转出来
#
# #新增印章页面
# iframe = driver.find_element(By.XPATH,"//*[@class='layui-layer-content']/iframe")
# driver.switch_to.frame(iframe)
# added5 = driver.find_element(By.XPATH,"//input[contains(@name,'fullName')]").send_keys("joel-(全称)-" + str(random.randint(0o01, 999)))
# added6 = driver.find_element(By.NAME,value='name').send_keys("joel-(简称)-"+ str(random.randint(0o01, 999)))
# sleep(2)
# """
# select类型下拉框
# select_by_index(index) ——通过选项的顺序，第一个为 0
# select_by_value(value) ——通过value属性
# select_by_visible_text(text) ——通过选项可见文本
#
# 取消方法
# deselect_by_index(index)
# deselect_by_value(value)
# deselect_by_visible_text(text)
# deselect_all()
#
# 非select标签
# # 先定位到下拉菜单
# ul = driver.find_element_by_css_selector("div#select2_container > ul")
# # 再对下拉菜单中的选项进行选择
# ul.find_element_by_id("li2_input_2").click()
#
# """
# drop = driver.find_element(By.XPATH,"//div[@class='layui-select-title']/input").click()
# sleep(2)
# added8 = driver.find_element(By.XPATH,"//dd[text()='测定实验🧫、、']").click()
# sleep(2)
#
# button2 = driver.find_element(By.ID,"submit").click()
# driver.switch_to.default_content()#跳转出来
# sleep(3)
#
#
# driver.switch_to.frame("pages_iframe")
# added10 = driver.find_element(By.CLASS_NAME,"com_so_input").send_keys("joel-002(全称)")
# button3 = driver.find_element(By.XPATH,"//a[text()='查询']").click()
#
#
# driver.quit()
