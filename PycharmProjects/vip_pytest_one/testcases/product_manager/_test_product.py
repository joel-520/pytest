import allure
import pytest
import requests

from commons.yaml_util import YamlUtil


@allure.epic("中国移动SAAS营销管理瓶体")
@allure.feature("用户管理模块")
class TestProduct:

    @allure.story("码尚教育接口")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("用例的描述1")
    @allure.link("接口访问的链接")
    @allure.issue("bug链接")
    @allure.testcase("测试用例链接")
    @pytest.mark.parametrize("caseinfo",YamlUtil("./testcases/product_manager/get_token.yaml").read_yaml())
    def test_get_token(self,caseinfo):

        names = caseinfo["name"]
        methods = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        datas = caseinfo["request"]["datas"]
        validates = caseinfo["validate"]

        allure.dynamic.title(names)

        res = requests.get(url=urls, params=datas)
        print(res.text)

    # @pytest.mark.parametrize("name,age", [["百里","35"],["北凡","34"]])
    # def test_aaa(self, name,age):
    #     print(name,age)