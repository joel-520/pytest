import json
import os

import yaml

class YamlUtil:

    #初始化对象的方法
    def __init__(self,yaml_path):
        self.yaml_path = yaml_path


    #读取yaml(用例）
    def read_yaml(self):
        with open(self.yaml_path,mode="r",encoding="utf-8") as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result
#
#     #写入yaml
#     def write_yaml(self,data):
#         with open(self.yaml_path, mode="w", encoding="utf-8") as f:
#             yaml.dump(data, stream=f,allow_unicode=True)
#
#     #清空
#     def clear_yaml(self):
#         with open(self.yaml_path, mode="w", encoding="utf-8") as f:
#             f.truncate()
# if __name__ == '__main__':
    # data = {'mashang': {'name': '百里老师', 'age': 35}, 'job': {'jobname': '老师', 'name': '百里老师', 'age': 35}}
    # YamlUtil().write_yaml("../testcases/uesr_manager/test_login.yaml")
    # print(YamlUtil().read_yaml("../testcases/uesr_manager/test_login.yaml"))
    # YamlUtil("../testcases/user_manager/test_login.yaml").clear_yaml()


# 读取yaml
def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml", mode="r", encoding="utf-8") as f:
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result[key]


# 写入yaml
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml", mode="a", encoding="utf-8") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空
def clear_yaml():
    with open(os.getcwd()+"/extract.yaml", mode="w", encoding="utf-8") as f:
        f.truncate()