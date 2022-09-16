# author：xintian   
# time:2020-06-13
#-*- coding: utf-8 -*-
from ip_config import HOST
import requests
api_url = f'{HOST}/api/mgr/sq_mgr/'
header = {'Content-Type': 'application/x-www-form-urlencoded'}#字典
#2- 参数--课程一定要有
payload = {
            'action':'add_teacher',
            'data':"""{
                        "username":"lishiming",
                        "password":"sq888",
                        "realname":"李世民",
                        "desc":"李世民老师",
                        "courses":[{"id":1099,"name":"接口自动化测试"}],
                        "display_idx":1
                    }"""
            }
reps = requests.post(api_url,data=payload)
reps.encoding = 'unicode_escape'#设置响应编码--显示中文

#fiddler-抓包看发出去是啥
#代码查看请求头
# print(reps.request.headers)
# #查看请求体
# print(reps.request.body)
print(reps.text)#打印响应内容--字符串类型