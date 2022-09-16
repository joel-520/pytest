# -*- coding: utf-8 -*-
# @Time : 2022/9/15 13:35
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: testcases/product_manager/test_mashang
# @Describe: ...
from pathlib import Path

import allure
import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil
current_path = str(Path(__file__).parent)

@allure.epic("项目名称：码尚商城接口测试")
@allure.feature("模块名称：用户管理模块测试")
class TestProductManager:
    # 登录测试用例
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('caseinfo', YamlUtil(current_path+"/test_login.yaml").read_yaml())
    def test_login(self, base_url, caseinfo):
        RequestUtil().standard_yaml_case(caseinfo, base_url)
        # print("Testing"+str(caseinfo))
        # print(caseinfo['story'])
        # print(caseinfo['title'])
        # print(caseinfo['request']['method'])
        # print(base_url + caseinfo['request']['url'])
        # print(caseinfo['request']['headers'])
        # print(caseinfo['request']['params'])
        # print(caseinfo['request']['data'])
        # print(caseinfo['validate'])
        # print(base_url)

        # method = caseinfo['request']['method']
        # url = base_url + caseinfo['request']['url']
        # headers = caseinfo['request']['headers']
        # params = caseinfo['request']['params']
        # data = caseinfo['request']['data']
        #
        # res = RequestUtil().send_all_request(url=url, method=method, json=data, params=params, headers=headers)
        # print(res.text)
        # token1 = re.search('"token":"(.*?)"',res.text)[1]
        # print("token1: " + str(token1))
        # print(res.json())
        # token2 = re.findall('"token":"(.*?)"',res.text)
        # print("token2: " + str(token2))
        #
        # result = res.json()
        # # token3 = jsonpath.jsonpath(result,"$.data.token")
        # # print("token3: %s" %token3)
        #
        # data = {"token": result['data']['token']}
        # write_yaml(data)

        # TestLogin.token = result['data']['token']
        # print("TestLogin.token: " + str(TestLogin.token))

        # print(res.json())
        # print(res.status_code)
        # print(res.headers)
        # print(res.cookies)
        # print(res.content)
        # print(res.encoding)

    # 订单列表
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('caseinfo', YamlUtil(current_path+"/test_order_list.yaml").read_yaml())
    def test_order_list(self, caseinfo, base_url):
        RequestUtil().standard_yaml_case(caseinfo, base_url)
    #     method = caseinfo['request']['method']
    #     url = base_url + caseinfo['request']['url']
    #     params = caseinfo['request']['params']
    #     params['token'] = read_yaml("token")
    #     data = caseinfo['request']['data']
    #
    #     res = RequestUtil().send_all_request(method=method, url=url, json=data, params=params)
    #     print(res.text)
    #