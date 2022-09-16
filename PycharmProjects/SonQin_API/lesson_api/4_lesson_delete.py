# author：xintian   
# time:2020-06-12
#-*- coding: utf-8 -*-
HOST='http://127.0.0.1:80'
import requests
api_url = f'{HOST}/api/mgr/sq_mgr/'

payload = {'action':'delete_course',
           'id':1100
           }
reps = requests.delete(api_url,data=payload)
reps.encoding = 'unicode_escape'
print(reps.text)