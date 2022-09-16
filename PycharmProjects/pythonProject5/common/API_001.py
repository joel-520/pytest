#1.导入requests库
import requests

#2.准备接口三要素
# 2.1 明确请求地址
url = "http://127.0.0.1：8000/api/departments/"
# 2.2 明确请求参数
# 2.3 发送请求+请求方式
response = requests.get（url=url）

# 查看返回值
print(response)


# 举例：
# 1.导入requests库
import requests

# 2.使用requests库
# 发送请求
response = requests.get('https://api.github.com/events')
# 查看结果
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.json())





"""
1.学习目标
    必须掌握requests库的基本使用
2.操作步骤
    # 1.导入requests库
    # 2.明确请求地址
    # 3.明确请求参数
    # 4.发送请求
3.需求
    使用requests库来请求学生管理系统一查询所有学院接口
4.总结
    返回值的获取
    response.text  # 获取返回值文本（将返回值以文本格式显示）
    response.json()  # 获取json格式的返回值，对于返回值类型为json格式比较友好
    response.status_code  # 获取状态码---HTTP协议响应状态码
    response.headers  # 获取响应头
    response.content # 获取响应源码（多用于爬虫）
5.json和python转化
    json.dumps(需要转换的python对象,indent=2,ensure_ascii=False)
        indent  表示格式化输出时缩进
        ensure_ascii=False 表示对非ascii字符不做转化
"""
# 1.导入requests库
import requests
import json

# 2.明确请求地址
url = "http://127.0.0.1:8000/api/departments/"

# 3.明确请求参数
# 没有参数不用写

# 4.发送请求
response = requests.get(url=url)
# print(response)
# 结果：<Response [200]>


# 5.获取返回值内容
res = response.json()  # 会获得一个字典格式的对象
print(type(res))  # <class 'dict'>

# 6.python字典转换为json字符串
# 使用json库实现

# 将python对象转换为json字符串
result = json.dumps(res, indent=2, ensure_ascii=False)
print(type(result))  # 字符串类型<class 'str'>
print(result)

# json.loads()  # 将json字符串转换为python对象


"""
结果：（简略，有17个，只展示两个，看看格式即可）
{
  "count": 17,
  "next": null,
  "previous": null,
  "results": [
    {
      "dep_id": "T02",
      "dep_name": "Java_2学院",
      "master_name": "Java-Master",
      "slogan": "java"
    },
    {
      "dep_id": "T03",
      "dep_name": "Java_3学院",
      "master_name": "Java-Master",
      "slogan": "java"
    }
}
"""
