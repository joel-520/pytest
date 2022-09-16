#coding = utf-8
from selenium import webdriver
import time

#1.打开浏览器
def open_broser(name,url):
    if name =='chrome':
        driver = webdriver.Chrome()
    elif name == 'firfox':
        driver = webdriver.Firefox()
    elif name == 'ie':
        driver = webdriver.Ie()
    driver.get("http://10.0.3.243:8088/")
    return driver
