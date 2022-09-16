# author：xintian   
# time:2020-06-14
#-*- coding: utf-8 -*-
#1- 获取token
import requests,json
def get_token():
    token_url = 'http://47.96.181.17:9090/rest/toController'
    payload = {"userName":"J201903070064","password":"362387359"}
    header = {'Content-Type':'application/json'}
    reps_token = requests.post(token_url,json=payload)
    #先转换成字典--通过键值取值
    token = json.loads(reps_token.text)['token']
    return token


#2- add_user
from random import randint
def add_user():
    tel = randint(11111111,99999999)
    adduser_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
    payload = {
                "aac003": "张三",
                "aac004": "1",
                "aac011": "21",
                "aac030": f"135{tel}",
                "aac01u": "88002255",
                "crm003": "1",
                "crm004": "1",
                "crm00a": "2018-11-11",
                "crm00b": "aaaaaa",
                "crm00c": "2019-02-28",
                "crm00d": "bbbbbb"
            }
    header = {'Content-Type':'application/json','X-AUTH-TOKEN':get_token()}
    reps_adduser = requests.post(adduser_url,json=payload,headers = header)
    print(reps_adduser.text)

