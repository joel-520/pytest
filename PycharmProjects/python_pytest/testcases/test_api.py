# -*- coding: utf-8 -*-
# @Time : 2022/9/6 9:12
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: testcases/test_api
# @Describe: ...
import allure
import pytest
import requests

# def setup():
#     print("Starting")
#
# def teardown():
#     print("Stopping")

@allure.epic("项目名称：测试章管家接口")
@allure.feature("模块名称：登录接口")
class TestLogin:

    # def setup(self):
    #     print("Starting server...")
    #
    # def teardown(self):
    #     print("Shutting down server...")

    @allure.story("接口名称：获取token接口")
    @allure.title("用例名称:验证获取token成功")
    @allure.description("Token获取")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.run(order=2)
    def test_get_token(self):
        # url = "http://10.0.3.243:8088/api/v3/getToken.htm?client_id=rTd9DUIYKQ&client_secret=NrL3EMcowTxmqQcYVepuEwd0ugNDzTRO&grant_type=code&response_type=json"
        # res = requests.get(url)
        # print(res.text)
        # TestLogin.token = res.json()["data"]["token"]
        allure.dynamic.title("Login Success")
        allure.dynamic.description("Login Success")
        print('TestLogin')

    # @pytest.mark.run(order=1)
    # @pytest.mark.skip("Test skip")
    # @pytest.mark.skipif(condition == "test", reason="Test skip")
    def test_login(self):
        print("Login successful")

        #增加用例执行步骤
        for i in range(1,5):
            with allure.step("第"+str(i)+"步：步骤如下："):
                print("执行第"+str(i)+"步")

        #添加用例附件
        # with open("E:\\666.png", mode="rb") as f:
        #     content = f.read()
        #     allure.attach(body=content,name="allure错误截图",attachment_type=allure.attachment_type.PNG)

        #添加文本
        allure.attach("http://localhost:8080/","接口测试地址",attachment_type=allure.attachment_type.TEXT)
        allure.attach("get","接口请求方式",attachment_type=allure.attachment_type.TEXT)
