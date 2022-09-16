import requests
from cfg import *



class Api:
    def list_1(self,grade=None):
        params = {
            'vcode': g_vcode,
            'action': 'list1'
        }
        if grade != None:
            params['grade'] = grade

        response = requests.get(g_api_path,params=params)
        body = response.json()
        print(body)
        return (body)




    def list_2(self, classid):

        payload = {
            'vcode': g_vcode,

        }

        url = f'{g_api_path}/{classid}'

        response = requests.delete(g_api_path,data=payload)
        body = response.json()
        print(body)
        return (body)