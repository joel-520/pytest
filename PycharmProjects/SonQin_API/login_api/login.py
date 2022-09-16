# author：xintian
# time:2020-06-13
#-*- coding: utf-8 -*-
import requests
def api_login(username,password):
    #1- 路径-url
    HOST = 'http://127.0.0.1:80'
    login_url = f'{HOST}/api/mgr/loginReq'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    payload = {'username':username,'password':password}
    reps = requests.post(login_url,data=payload)
    reps.encoding = 'unicode_escape'#设置响应编码--显示中文
    # return reps.cookies
    # print(reps.cookies)
    # print(reps.cookies['sessionid'])
    return reps.cookies['sessionid']


    # print(reps.text)#打印响应内容--字符串类型
#reps.requests.herders---请求头
#1- 查看下cookie
# print(reps.headers)#响应头
# print(reps.cookies)#打印cookies对象--jar格式

#2- cookie自定义--获取完set_cookie----自己加参数

#1- 直接传
if __name__ ==  "__main__":
    api_login('auto', 'sdfsdfsdf')