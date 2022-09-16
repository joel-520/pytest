# author：xintian   
# time:2020-06-14
#-*- coding: utf-8 -*-
#1------------------------- get_token--获取token--------------------
#密码需要加密--md5
import hashlib#算法库
import json
#hashlib.md5(b'')一定是byte
psw = hashlib.md5(b'zr111111hg').hexdigest()#获取16进制的值
print(psw)
import requests
token_url = 'http://121.41.14.39:2001/token/token'
payload = {'mobile':'13588000000','password':psw}
reps_token = requests.post(token_url,data=payload)
print(reps_token.text)
usr_token = json.loads(reps_token.text)['data']


#2------------------------- file upload--获取token--------------------
file_url = 'http://121.41.14.39:2001/user/doUpload'
#cookie---需要自己封装
user_cookie = {'token':usr_token}
#(文件的名字，文件对象，类型)
fileload = {'file':('logo.png',open(r'C:\Users\XinTian\Desktop\logo.png','rb'),'jpg/png/gif')}
reps_file = requests.post(file_url,files = fileload,cookies = user_cookie)
print(reps_file.text)
import pprint#完美打印
pprint.pprint(reps_file.json())
