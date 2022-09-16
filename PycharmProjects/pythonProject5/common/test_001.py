"""
send_method.py 文件说明：
1，封装接口请求方式
    根据项目接口文档提供的内容进行封装
    不同的项目，sendmethod也不太一样，如请求体格式等。
2.封装思路-结合接口三要素
    请求方式+请求地址
    请求参数
    返回值
3.以学生管理系统SMS为例:
    结合学生管理系统项目的接口文档，封装SendMethod类

"""
# 导入所需模块
import requests
import json


# 封装请求模块
class SendMethod:
    """
        结合学生管理系统SMS，请求方式包括如下:
            get ---> parmas标准请求参数
            post--->请求参数类型 json
            put --->请求参数类型 json
            delete ---> parmas标准请求参数
    """

    # 定义该方法为静态方法
    @staticmethod
    def send_method(method, url, parmas=None, json=None):
        """
        封装适用于学生管理系统项目的接口请求
        :param method: 请求方式
        :param url: 请求地址
        :param parmas: get和delete请求参数
        :param json: post和put请求参数
        :param headers: 请求头
        :return:
        """
        # 定义发送请求的方法
        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, params=parmas)
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, json=json)
            # 如果有不同的请求头，还可以继续添加接收的参数
            # response = requests.request(method=method, url=url, json=json, data=data, files=data)
        else:
            # 这里是简单处理，完成封装需要加上异常处理。
            response = None
            print("请求方式不正确")

        # 如果请求方式是delete，只返回状态码
        # 这是根据项目接口文档中delete方法的返回规则定的。
        if method == "delete":
            return response.status_code
        else:
            # 项目中接口的返回值是json格式的，就可以用json()进行格式化返回结果。
            return response.json()

    @staticmethod
    def json_2_python(res):
        """
        格式化返回数据
        :param res:接口返回的数据
        :return:
        """
        return json.dumps(res, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    method = "post"
    url = "http://127.0.0.1:8000/api/departments/"
    data = {
        "data": [
            {
                "dep_id": "T02",
                "dep_name": "接口测试学院",
                "master_name": "Test-Master",
                "slogan": "Here is Slogan"
            }
        ]
    }
    res = SendMethod.send_method(method=method, url=url, json=data)
    # print(res)
    print(SendMethod.json_2_python(res))

    # method = "get"
    # params = {"$dep_id_list": "1, 2, 3"}
    # res = SendMethod.send_method(method=method, url=url, json=data)
    # print(SendMethod.json_2_python(res))
