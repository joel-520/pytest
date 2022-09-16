# 1.导入appium
import time
from appium import webdriver

# 2.创建Desired capabilities对象，添加启动参数
desired_caps = {
    "platformName": "Android",  # 系统名称
    "platformVersion": "7.1.2",  # 系统版本
    "deviceName": "127.0.0.1:21503",  # 设备名称
    "appPackage": "com.android.settings",  # APP包名
    "appActivity": ".Settings"  # APP启动名
}

# 3.启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 4.操作APP
# 获取当前页面源码
# 只是设置首页中的页面源码
source = driver.page_source
# # print(source)

# 将APP的页面源码保存到一个文件中
with open("source.txt", "w", encoding="UTF-8") as fp:
    fp.write(source)

# 从管理app页面中打开文件管理器app
# 先用adb命令获取文件管理器的包名和启动名
# com.cyanogenmod.filemanager/.activities.NavigationActivity
driver.start_activity("com.cyanogenmod.filemanager", ".activities.NavigationActivity")


# 将应用置于后台运行(5秒)
# 提示：测试前最好把所有后台运行的APP都关掉
driver.background_app(5)


# 5.关闭APP
time.sleep(3)
driver.quit()


