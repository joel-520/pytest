import json

from pip._vendor import requests


class AllRequest:
    session = requests.session()

    def all_send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            res = AllRequest.session.request(method=method, url=url, params=data, **kwargs)
        elif method == "post":
            strdata = json.dumps(data)
            res = AllRequest.session.request(method=method, url=url, data=strdata, **kwargs)
        else:
            print("不支持的请求方式")
        return res