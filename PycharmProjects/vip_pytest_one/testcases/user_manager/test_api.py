# -*- coding: utf-8 -*-
# @Time : 2022/9/5 9:25
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: testcases/user_manager/test_api
# @Describe: ...
import os
import re
from pathlib import Path

import allure
import pytest

from commons.yaml_util import YamlUtil, write_yaml, read_yaml
from commons.request_util import RequestUtil

current_path = str(Path(__file__).parent)



@allure.epic("项目名称：码尚商城接口测试")
@allure.feature("模块名称：用户管理模块测试")
class TestLogin:

    # 访问phpwind论坛首页接口
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('caseinfo', YamlUtil(current_path+"/test_phpwind_start.yaml").read_yaml())
    def test_phpwind_start(self, caseinfo):
        RequestUtil().standard_yaml_case(caseinfo, "")
    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']
    #     res = RequestUtil().send_all_request(url=url, method='get')
    #     # print(res.text)
    #     csrf_token = {"csrf_token": re.search('name="csrf_token" value="(.*?)"/', res.text)[1]}
    #     write_yaml(csrf_token)
    #
    #     print("csrf_token: ", csrf_token)
    #     # TestLogin.cookies = re.cookies
    #
    #登录pypwind
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('caseinfo', YamlUtil(current_path+"/test_login_phpwind.yaml").read_yaml())
    def test_login_phpwind(self,caseinfo):
        RequestUtil().standard_yaml_case(caseinfo, "")
    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']
    #     headers = caseinfo['request']['headers']
    #     data = caseinfo['request']['data']
    #     data['csrf_token'] = read_yaml('csrf_token')
    #     res = RequestUtil().send_all_request(url=url, method=method, data=data, headers=headers)
    #     print(res.text)
