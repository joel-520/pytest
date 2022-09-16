"""
    封装公共方法
"""
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, browser="chrome"):
        """
        初始化driver
        :param browser:浏览器名称
        """
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            self.driver = None
            print("请输入正确的浏览器,例如:chrome,firefox,ie")

    def open_url(self, url):
        """
        打开地址
        :param url: 被测地址
        :return:
        """
        self.driver.get(url)
        time.sleep(2)

    def find_element(self, locator, timeout=10):
        """
        定位单个元素,如果定位成功返回元素本身,如果失败,返回False
        :param locator: 定位器,例如("id","id属性值")
        :return: 元素本身
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"{locator}元素没找到")
            return False

    def click(self, locator):
        """
        点击元素
        :return:
        """
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        """
        关闭浏览器
        :return:
        """
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    base = Base()
    base.open_url("http://10.0.3.243:8088/")
    base.close()








"""
    管理登陆页面所有的元素，
    以及操作这些元素所用的方法。
"""
from common.base import Base


class LoginPage(Base):
    # 编写定位器和页面属性
    name_input_locator = ("id", "name")
    passwd_input_locator = ("id", "password")
    submit_button_locator = ("id", "submit")
    username = 'xxxxxxxxxxx'
    userpasswd = 'xxxxxx'
    url = 'https://sso.kuaidi100.com/sso/authorize.do'

    # """封装元素操作"""
    # 输入用户名
    def name_imput(self):
        self.send_keys(self.name_input_locator, self.username)

    # 输入密码
    def passwd_imput(self):
        self.send_keys(self.passwd_input_locator, self.userpasswd)

    # 点击登陆
    def click_submit(self):
        self.click(self.submit_button_locator)


if __name__ == '__main__':
    base = Base('firefox')
    base.open_url(url=LoginPage.url)





# 1. 导入包
import unittest
from pages.login_page import LoginPage


# 定义测试类
class TestCaseLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = LoginPage()
        self.driver.open_url(LoginPage.url)

    def tearDown(self) -> None:
        # 5. 关闭浏览器
        self.driver.close()

    def testLogin(self):
        """登陆测试用例"""
        self.driver.name_imput()
        self.driver.passwd_imput()
        self.driver.click_submit()


if __name__ == '__main__':
    unittest.main()
