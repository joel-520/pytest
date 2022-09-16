from time import sleep

import pytest
import requests
from pytest_html.extras import json


def read_yaml(param):
    pass


class TestLogin:
    token = " "
    session = requests.Session()

    @pytest.mark.parametrize("castinfo",read_yaml("get_token.yaml"))
    def test_01_baili(self,castinfo):
        print(castinfo['name'])
        print(castinfo['request']['method'])
        print(castinfo['request']['url'])
        print(castinfo['request']['params'])
        print(castinfo['request']['validate'])

        url = castinfo['request']['url']
        params = castinfo['request']['params']
        method = castinfo['request']['method']
        res = TestLogin.session.request(method,url=url,params=params)
        # 把数据合成dict字典并写入yaml文件
        if "token" in res.text:
            extranct_data = {"token": res.json(['token'])}
            # write_yaml(extranct_data)
        print(res.text)

        @pytest.mark.parametrize("castinfo", read_yaml("get_token.yaml"))
        def test_01_baili(self, castinfo):
            print(castinfo['name'])
            print(castinfo['request']['method'])
            print(castinfo['request']['url'])
            print(castinfo['request']['params'])
            print(castinfo['request']['validate'])

            url = castinfo['request']['url']
            params = castinfo['request']['params']
            method = castinfo['request']['method']
            res = TestLogin.session.request(method, url=url, params=params)
            # 把数据合成dict字典并写入yaml文件
            if "token" in res.text:
                extranct_data = {"token": res.json(['token'])}
                # write_yaml(extranct_data)
            print(res.text)

        @pytest.mark.parametrize("castinfo", read_yaml("post.yaml"))
        def test_01_baili(self, castinfo):

            url = castinfo['request']['url']+read_yaml("token")
            value = castinfo['request']['json']
            method = castinfo['request']['method']
            res = TestLogin.session.request(method, url=url, json=json)
            # 把数据合成dict字典并写入yaml文件
            if "token" in res.text:
                extranct_data = {"token": res.json(['token'])}
                # write_yaml(extranct_data)
            print(res.text)
