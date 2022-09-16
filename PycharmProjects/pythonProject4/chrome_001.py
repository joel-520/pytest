from selenium import webdriver

# 加启动配置

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

# return webdriver.Chrome(chrome_options = option,desired_capabilities = None)
# 打开chrome浏览器

driver = webdriver.Chrome(chrome_options=option)
driver.get("http://10.0.3.243:8088")