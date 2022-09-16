# author：xintian   
# time:2020-06-12
#-*- coding: utf-8 -*-
import requests
Host = 'http://127.0.0.1:80'
api_url = f'{Host}/apijson/mgr/sq_mgr/'
header = {'Content-Type': 'application/json'}#字典
#2- 参数
payload = {
            'action':'add_course_json',
            'data':{
                    "name":"心田",
                    "desc":"初中化学课程",
                    "display_idx":"2"
                    }
            }
reps = requests.post(api_url,json=payload)
reps.encoding = 'unicode_escape'#设置响应编码--显示中文

#fiddler-抓包看发出去是啥
#代码查看请求头
# print(reps.request.headers)
# #查看请求体
# print(reps.request.body)
print(reps.text)#打印响应内容--字符串类型