# 1.导入appium
import time
from appium import webdriver

# 2.创建Desired capabilities对象，添加启动参数
desired_caps = {
    "platformName": "Android",  # 系统名称
    "platformVersion": "7.1.2",  # 系统版本
    "deviceName": "127.0.0.1:21503",  # 设备名称
    "appPackage": "com.microvirt.launcher2",  # APP包名
    "appActivity": "com.microvirt.launcher.Launcher"  # APP启动名
}

# 3.启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


# 4.操作APP
# 脚本机器中APK⽂件路径
app_path = r'C:\Users\L\Desktop\com.taobao.taobao_V9.15.0.apk'
# 安装apk
driver.install_app(app_path)
time.sleep(5)

# 要知道即将卸载的APP的包名
bundle_id = "com.taobao.taobao"
result = driver.is_app_installed(bundle_id)
# 参数：
#   bundle_id: 传⼊app包名,返回结果为True(已安装) / False(未安装)
print(result)

# 5.关闭APP
time.sleep(3)
driver.quit()
