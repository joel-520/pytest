from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

option = webdriver.ChromeOptions()

# 1.新版本谷歌浏览器-解决控制提示
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])

chrome_driver_path = "C:\Python39\chromedriver.exe"
options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument("user-data-dir=C:\\Program Files\\Google\\Chrome\\User Data\\Profile 8")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


driver.get(url="http://10.0.3.243:8088")
sleep(5)
driver.quit()