# author：xintian   
# time:2020-06-12
#-*- coding: utf-8 -*-
import requests
# from login_api.login import user_cookie
from login_api.login import api_login
user_session= api_login('auto','sdfsdfsdf')
user_cookie = {'sessionid':user_session}#自己封装
#1- 路径-url
HOST = 'http://127.0.0.1:80'
api_url = f'{HOST}/api/mgr/sq_mgr/'
header = {'Content-Type': 'application/x-www-form-urlencoded'}#字典
#2- 参数
payload = {
            'action':'add_course',
            'data':"""{
                    "name":"心田",
                    "desc":"初中化学课程",
                    "display_idx":"2"
                    }"""
            }
reps = requests.post(api_url,data=payload,cookies = user_cookie)
reps.encoding = 'unicode_escape'#设置响应编码--显示中文

'''
为什么需要自定义cookie
商城项目：性能班---保证vip权限
在cookie--登录成功--必须带一个token（松勤vip账号--获取的）



'''




print(reps.request.headers)#代码查看请求头
# print(reps.request.body)#查看请求体
print(reps.text)#打印响应内容--字符串类型

'''
1- json参数---建议使用
reps = requests.post(api_url,json=payload2)

2- data参数
import json
reps = requests.post(api_url,data=json.dumps(payload2),headers = header)
'''