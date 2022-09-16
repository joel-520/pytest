import os

import yaml


class DebugTalk:

    # 读取yaml
    def read_yaml(self,key):
        with open(os.getcwd() + "/extract.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(f, Loader=yaml.FullLoader)

            return result[key]

    # 读取yaml
    def read_yamls(self,key,index):
        with open(os.getcwd() + "/extract.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            return result[key][int(index)]
