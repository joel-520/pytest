# 1.导入requests库
import json
import requests

# 2.明确请求地址
# url = "http://127.0.0.1:8000/api/departments/"
url = "http://10.0.3.243:8088/get"
# 3.明确请求参数
# 是一个字典类型数据
data = {"$dep_id_list": "10,11"}

# 明确请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"}


# 设置代理服务器地址
# 如果发送的是http请求，就使用http请求的代理，如果发送的是https请求，就使用一个https请求的代理。
proxies = {"https": "https://58.220.95.86:9401", "http": "http://113.214.13.1:1080"}

# 发送请求
response = requests.get(url=url, headers=headers, proxies=proxies)
# 查看响应结果的状态码
print(response.status_code)
# 获得响应结果的源码
print(response.text)
# 4.发送请求
response = requests.get(url=url, params=data, headers=headers)
# print(response.json())

# 将python对象转换为json字符串（格式化放回数据）
result = json.dumps(response.json(), indent=2, ensure_ascii=False)
# print(type(result))  # 字符串类型
print(result)

"""
接口返回结果：可以看到User-Agent属性变成了我们设置的内容了。
{
  "args": {
    "$dep_id_list": "10,11"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Host": "127.0.0.1:9999",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
  },
  "origin": "127.0.0.1",
  "url": "http://127.0.0.1:9999/get?%24dep_id_list=10%2C11"
}

"""