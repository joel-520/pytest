# -*- coding: utf-8 -*-
# @Time : 2022/8/29 8:52
# @Author : joel
# @Email : 770546904@qq.com
# @File : test_login.py
import allure
import pytest


@allure.epic("项目名称：allure测试")
@allure.feature("模块名称：allure测试接口")
class TestLogin:

    a=8


    @allure.story("接口名称：Login")
    @allure.title("用例名称：Login登录")
    @allure.description("测试登录")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("http://localhost:8080/")
    @allure.testcase("用例连接")
    @pytest.mark.smoke
    def test_login(self):
        print('登录用例')

        #增加用例执行步骤
        for i in range(1, 5):
            with allure.step("第"+str(i)+"步: 步骤如下："):
                print("执行第"+str(i)+"步")

        #增加用例附件
        with open("E:\\666.png", "rb") as f:
            content = f.read()
            allure.attach(body=content,name="allure错误截图",attachment_type=allure.attachment_type.JPG)

        #加文本
        allure.attach("http://localhost:8080","allure接口地址",attachment_type=allure.attachment_type.TEXT)
        allure.attach("get","allure请求方式",attachment_type=allure.attachment_type.TEXT)

    @allure.story("接口名称：Register接口")
    def test_register(self):
        allure.dynamic.title("用例名称：Register")
        allure.dynamic.description("描述：Register验证")
        print('注册用例')

    @pytest.mark.joel
    # @pytest.mark.skip(reason='反例跳过')
    @pytest.mark.skipif(a<10,reason='跳过')
    def test_order_list(self):
        print('商品订单用例')