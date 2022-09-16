import random


class DebugTalk:

    # 获取随机数的方法
    def get_random_number(self, min, max):
        return random.randint(int(min), int(max))

    # 获取extract.yaml文件中的值
    def get_extract_data(self, node_name):
        return read_extract_file(node_name)

    # 获取extract.yaml文件中的值
    def get_base_url(self, node_name):
        return read_config_file_file('base', node_name)