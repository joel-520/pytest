from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': '90722a37',

                'platformVersion': '7.1.2',

                # apk包名

                'appPackage': 'com.shjysoft.console',

                # apk的launcherActivity

                'appActivity': 'cmp=com.shjysoft.console/.commonment.LoginActivity'

                }

# Remote 地址在 Appuim 里找
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)