from selenium import webdriver
# 加启动配置
option = webdriver.ChromeOptions()

# 1.新版本谷歌浏览器-解决控制提示
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])

# 2.旧版本浏览器-解决控制提示（待测试）
# option.add_argument('disable-infobars')

# 解决密码提示
prefs = {"": ""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
option.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=CHROME_PATH,chrome_options=option)
