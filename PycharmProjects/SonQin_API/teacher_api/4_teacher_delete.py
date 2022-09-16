# author：xintian   
# time:2020-06-13
#-*- coding: utf-8 -*-
from ip_config import HOST
import requests
api_url = f'{HOST}/api/mgr/sq_mgr/'

payload = {'action':'delete_teacher',
           'id':243
           }
reps = requests.delete(api_url,data=payload)
reps.encoding = 'unicode_escape'
print(reps.text)