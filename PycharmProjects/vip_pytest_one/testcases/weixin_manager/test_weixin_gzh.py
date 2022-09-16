# -*- coding: utf-8 -*-
# @Time : 2022/9/5 11:26
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: testcases/weixin_manager/test_login
# @Describe: ...
from pathlib import Path

import pytest
import requests



from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil
current_path = str(Path(__file__).parent)

class TestGzh:
    # 1.获取鉴权码access token接口
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('caseinfo', YamlUtil(current_path + "/test_get_access_token.yaml").read_yaml())
    def test_get_access_token(self, caseinfo):
        RequestUtil().standard_yaml_case(caseinfo, "")

    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']
    #     params = caseinfo['request']['params']
    #
    #     res = RequestUtil().send_all_request(url=url, method=method, params=params)
    #     data = {"access_token": res.json()['access_token']}
    #     write_yaml(data)
    #     print(res.text)
    #     # print(TestLogin.access_token)
    #
    # 2.微信公众号文件上传接口
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('caseinfo', YamlUtil(current_path + "/test_file_upload.yaml").read_yaml())
    def test_file_upload(self, caseinfo):
        RequestUtil().standard_yaml_case(caseinfo, "")
    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']
    #     params = {}
    #     params['access_token'] = read_yaml('access_token')
    #     files = caseinfo['request']['files']
    #     print(files)
    #     files["media"] = open(files["media"], mode='rb')
    #     print(files["media"])
    #     res = RequestUtil().send_all_request(url=url, method=method, params=params, files=files)
    #     print(res.text)
