from selenium import webdriver
# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 改动打开浏览器

driver = webdriver.Chrome(chrome_options=option)

#最后完整脚本如下：

# coding = utf-8
import time
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 打开chorme浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[@id='kw']").send_keys('selenium')
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(3)
driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()
driver.quit()