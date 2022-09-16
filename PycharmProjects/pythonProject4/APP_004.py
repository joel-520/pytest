# 1.导入appium
import time
from appium import webdriver
import base64

# 2.创建Desired capabilities对象，添加启动参数
desired_caps = {
    "platformName": "Android",  # 系统名称
    "platformVersion": "7.1.2",  # 系统版本
    "deviceName": "127.0.0.1:21503",  # 设备名称
    "appPackage": "com.cyanogenmod.filemanager",  # APP包名
    "appActivity": ".activities.NavigationActivity"  # APP启动名
}

# 3.启动APP
# 声明手机驱动对象(实例化webdriver)
# 第一个参数为appium服务的地址，需要启动appium服务。
# 第二个参数为Desired capabilities对象
# 我们就先传入这两个参数就可以了。
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 4.操作APP

# 4.1 发送文件到手机
file_path = r'C:\Users\L\Desktop\test.txt'

# 将文件转换成二进制文件
with open(file_path, 'rb') as fp:
    data = str(base64.b64encode(fp.read()), 'utf-8')
    # print(data)

# 将转换格式的文件发送到手机
path = r'/sdcard/test.txt'
driver.push_file(path, data)

# 4.2 从手机中拉取文件到电脑上
# 手机中文件的路径
path_app = '/sdcard/test.txt'
# 返回数据为base64编码的数据
data = driver.pull_file(path_app)

print(data)

# base64解码
with open('test.txt', 'wb') as fp:
    fp.write(base64.b64decode(data))

# 提示：该文件会拉取到脚本文件所在的目录中

# 5.关闭APP
time.sleep(5)
driver.quit()