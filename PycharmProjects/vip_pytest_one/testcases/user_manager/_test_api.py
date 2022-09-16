import allure


@allure.epic("中国移动SAAS营销管理瓶体")
@allure.feature("用户管理模块")
class TestApi:

    @allure.story("码尚教育接口")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("用例的描述1")
    @allure.link("接口访问的链接")
    @allure.issue("bug链接")
    @allure.testcase("测试用例链接")
    def aatest_mashang(self,base_url):
        allure.dynamic.title("测试码尚教育正例2")
        #allure.dynamic.description("用例的描述2")
        print(base_url+"码尚教育")
        for a in range(1,11):
            with allure.step("测试用例的第"+str(a)+"步"):
                pass
        with allure.step("接口名称：XXX"):
            pass
        with allure.step("接口地址：XXX"):
            pass
        #错误截图
        with open("E:\\shu.jpg",mode="rb") as f:
            allure.attach(body=f.read(), name="登陆错误截图", attachment_type=allure.attachment_type.JPG)
        assert 'a' in 'abc'
