# author：xintian   
# time:2020-06-12
#-*- coding: utf-8 -*-
HOST='http://127.0.0.1:80'
import requests
api_url = f'{HOST}/api/mgr/sq_mgr/'

payload = {'action':'modify_course',
           'id':1100,
            'newdata':'''{
            "name":"松勤",
            "desc":"心田老师课程",
            "display_idx":"5"
            }'''
         }
reps = requests.put(api_url,data=payload)
reps.encoding = 'unicode_escape'
print(reps.text)
# # print(reps.json(),width =60)
# import pprint
# pprint.pprint(reps.json(),width =60)