import time

import pytest
import requests


class TestApi:

    accessToken = ''

    def test_get_token(self):
        url = "http://10.0.3.243:8088/api/getToken.htm"
        params = {
            "client_id": "xSsKbNaQYe",
            "client_secret": "3sdqAsxIBhJqs2zvmjC5mfgEL43Sxowe",
            "grant_type": "code",
            "response_type": "json"
        }

        res = requests.get(url=url,params=params)
        TestApi.accessToken = res.json()['accessToken']
        # 拼接最终的token，注意中间有个空格
        TestApi.accessToken = "Bearer" + " " + TestApi.accessToken
    #     # print("token:",res.json(['accessToken']))
    #
    #     # 把数据合成dict字典并写入yaml文件
    #     # if "token" in res.text:
    #     #     extranct_data = {"token": res.json(['token'])}
    #     #     # write_yaml(extranct_data)
        print(res.text)
        print(TestApi.accessToken)

    def test_batch_create(self):
        url = "http://10.0.3.243:8088/api/sealApply/batchCreate.htm"
        data = [
            {
                "file_count": "1",
                "uid": "18117495115",
                "seal_ids1": "ff8080817a3ce063017a3d33f66c02ea",
                "use_count1": "10",
                "is_sealed_bid1": "fasle",
                "code": "20215" + str(int(time.time())),
                "apply_reason": "测试555666",
                "sealapply_id": "2c9070f47a3cf" + str(int(time.time()*1000)),
                "type_id": "8a8083506125bae6016146241e2c1005",
                "name": "api测试-" + str(int(time.time())),
                "department_id": "",
                "apply_status": "6",
                "contract_price": "3111333",
                "customers_name": "往来单位111222",
                "customers_id": "",
                "operateTime": "",
                "use_person": ""
            }

        ]


        headers = {
            "Authorization": TestApi.accessToken
        }


        res = requests.post(url=url,json=data,headers=headers)
        print(res.text)

    # def test_file_upload(self):
    #     url = "http://10.0.3.243:8088/api/sealApply/uploadFileByUrl.htm"
    #     value = {
    #         "sealapply_id": "202151642048009",
    #          "filement": [{
    #              "downLoadUrl": "http://10.0.3.142:8099/1.docx",
    #              "fileName": "1.docx",
    #              "is_watermark": "1"
    #          },
    #              {
    #                  "downLoadUrl": "http://10.0.3.142:8099/2.PDF",
    #                  "fileName ": "2.PDF",
    #                  "is_watermark": "1"
    #              }
    #          ],
    #     }
    #
    #     headers = {
    #         "Authorization": TestApi.accessToken
    #     }
    #
    #     res = requests.post(url=url,json=value,headers=headers)
    #     print(res.text)


if __name__ == '__main__':
    pytest.main()