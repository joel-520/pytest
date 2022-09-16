# author：xintian   
# time:2020-06-12
#-*- coding: utf-8 -*-
HOST='http://127.0.0.1:80'
import requests
api_url = f'{HOST}/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=2'

payload = {'action':'add_course',
            'data':'''{
            "name":"初中化学",
            "desc":"初中化学课程",
            "display_idx":"4"
            }'''
         }
reps = requests.get(api_url)
reps.encoding = 'unicode_escape'
# print(reps.json(),width =60)
import pprint
pprint.pprint(reps.json(),width =60)
