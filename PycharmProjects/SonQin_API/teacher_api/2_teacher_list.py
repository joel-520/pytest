# author：xintian   
# time:2020-06-13
#-*- coding: utf-8 -*-
from ip_config import HOST
import requests
api_url = f'{HOST}/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20'
header = {'Content-Type': 'application/x-www-form-urlencoded'}#字典


reps = requests.get(api_url)
reps.encoding = 'unicode_escape'#设置响应编码--显示中文
print(reps.text)
import pprint
pprint.pprint(reps.json(),width =60)