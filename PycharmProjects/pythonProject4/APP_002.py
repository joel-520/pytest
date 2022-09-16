"""
1.学习目标
    掌握appium启动手机方法
2.操作步骤
    1-说明：明确驱动对象(操作对象)
    web自动化步骤：
        1.指定启动浏览器
        2.输入网址
        3.继续其他操作...

    APP自动化步骤：
        要先传递如下信息：
            系统名称: Android  IOS
            系统版本: 版本号
            设备名称: 通过adb devices命令获取
            APP包名:  打开哪个APP
            APP启动名:进入APP哪个页面

    2-导入appium中webdriver
    3-添加启动参数
        设备信息
            系统名称: Android  IOS
            系统版本: 版本号
            设备名称: adb devices
        APP信息
            APP包名:  打开哪个APP
            APP启动名:进入APP哪个页面
     4-启动app
     	webdriver.Remote()
     5-操作app
     6-关闭app
3.需求
    启动Android模拟器中的设置APP
"""

# 1.导入appium
import time
from appium import webdriver

# 2.添加启动参数
# 就是Desired capabilities，是一个字典类型的对象。
desired_caps = {
    "platformName": "Android",  # 系统名称
    "platformVersion": "10.0",  # 系统版本
    "deviceName": "90722a37",  # 设备名称
    "appPackage": "com.shjysoft.privatecloud",  # APP包名
    "appActivity": "com.shjysoft.commonment.TabActivity"  # APP启动名
}

"""
说明：
deviceName ：
    cmd进入命令行终端
    输入adb connect 127.0.0.1:62001 链接夜神模拟器
    输入adb devices 获取设备名称

appPackage和appActivity获取：
    首先在虚拟机中打开设置
    输入命令adb shell dumpsys window windows | findstr mFocusedApp
    在u0之后的就是包名和启动名com.android.settings/.Settings

"""

"""
提示：
platformName字段中Android和android大小写都可以。
deviceName 字段，在测试Android手机时，随意写都可以，比如123
    因为deviceName字段是针对IOS系统的，
    对于Android系统，该字段必须要有，但是内容可以随意写，且不能为空。

platformVersion 字段写两位也可以，能够运行。
"""

# 3.启动APP
# 声明手机驱动对象(实例化webdriver)
# 第一个参数为appium服务的地址，需要启动appium服务。
# 第二个参数为Desired capabilities对象
# 我们就先传入这两个参数就可以了。
driver = webdriver.Remote("http://10.0.3.142:4723/wd/hub", desired_caps)

# http://0.0.0.1:4723/wd/hub 中/wd/hub这个是固定的，必须有，要求的。
# 上面的一步就已经把app启动起来了。

# 4.操作APP
# 先不对app做任何操作。

# 5.关闭APP
time.sleep(5)
driver.quit()
