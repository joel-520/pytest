#Python+unittest+requests+HTMLTestRunner完整的接口自动化测试框架搭建_05——参数动态化
import readConfig as readConfig

readconfig = readConfig.ReadConfig()


class geturlParams():  # 定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + '/login' + '?'
        # logger.info('new_url'+new_url)
        return new_url


if __name__ == '__main__':  # 验证拼接后的正确性
    print(geturlParams().get_Url())
