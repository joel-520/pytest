from selenium import webdriver
from selenium.webdriver.chrome.options import Options


option = webdriver.ChromeOptions()
#加上下面两行，解决报错
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避
bugchrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败#
chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" #手动指定使用的浏览器位置
driver=webdriver.Chrome(chrome_options=chrome_options)#executable_path驱动路径
driver.get('http://www.baidu.com')
print(driver.page_source)




