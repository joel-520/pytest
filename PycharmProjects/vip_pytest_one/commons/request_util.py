# -*- coding: utf-8 -*-
# @Time : 2022/9/8 9:49
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: /send_all_requests
# @Describe: ...
import re
from io import StringIO

import jsonpath
import yaml
import requests

from commons.assert_util import assert_result
from commons.yaml_util import write_yaml
from hotloads.debug_talk import DebugTalk


class RequestUtil:

    sess = requests.Session()

    #标准化yaml测试用例
    def standard_yaml_case(self, caseinfo,base_url):

        #在请求之前调用热加载，通过反射使得yaml能够调用Python里面的函数
        yaml_str = yaml.dump(caseinfo)
        yaml_str = self.replace_hotload(yaml_str)
        caseinfo = yaml.safe_load(StringIO(yaml_str))

        #标准化yaml
        case_keys = caseinfo.keys()
        # print(case_keys)
        #如果后者"title","request","validate"的超集是set(case_keys)则返回true
        if set(case_keys).issuperset({"title","request","validate"}):
            return_keys = caseinfo["request"].keys()
            # print(return_keys)
            #判断request目录下必须有method","url"
            if set(return_keys).issuperset({"method","url"}):
                # print("Request 用例格式正确")
                #处理url
                caseinfo["request"]["url"] = base_url + caseinfo["request"]["url"]
                #处理files
                for key, value in caseinfo["request"].items():
                    if key == 'files':
                        for file_key, file_value in value.items():
                            value[file_key] = open(file_value, 'rb')
                #发送请求
                res = self.sent_allrequest(**caseinfo["request"])
                print(res.text)
                # @提取中间变量
                self.extract_yaml_value(caseinfo,res)
                #断言封装
                if caseinfo["validate"]:
                    assert_result(caseinfo["validate"],res)


            else:
                print("Request yaml中的request目录下必须包含method,url")
        else:
            print("Request yaml中必须包含title,request,validate")

    #封装的统一发送请求的方法
    def sent_allrequest(self,**kwargs):

        res = RequestUtil.sess.request(**kwargs)
        # for key, value in kwargs.items():
        #     if key == 'files':
        #         for file_key, file_value in value.items():
        #             value[file_key] = open(file_value, 'rb')
        return res

 #提取中间变量保存到extract.yaml

    def extract_yaml_value(self,caseinfo,res):
        if "extract" in caseinfo.keys():
            for key,value in caseinfo['extract'].items():
                #正则提取
                if "(.*?)" in value or "(.+?)":
                    zz_value = re.findall(value, res.text)
                    # print(zz_value)
                    if len(zz_value) == 0:
                        print("没有提取到任何值！")
                    else:
                        if zz_value == 1:
                            # 提取到一个值
                            data = {key:zz_value[0]}
                            write_yaml(data)

                        else:
                            # 提取到多个值
                            data = {key: zz_value}
                            write_yaml(data)
                else:
                    #json提取
                    js_value = jsonpath.jsonpath(res.json(), value)
                    # print(js_value)
                    if js_value:
                        if len(js_value) == 1:
                            data = {key: js_value[0]}
                            write_yaml(data)
                        else:
                            data = {key:js_value}
                            write_yaml(data)

    #热加载
    def replace_hotload(self,yaml_str):
        regexp = "\\${(.*?)\\((.*?)\\)}"
        fun_list = re.findall(regexp, yaml_str)
        for f in fun_list:
            if f[1] == "":
                new_value = getattr(DebugTalk(), f[0])()

            else:
                new_value = getattr(DebugTalk(),f[0])(*f[1].split(','))
            oldstr = "${"+f[0]+"("+f[1]+")}"
            yaml_str = yaml_str.replace(oldstr,str(new_value))
        return yaml_str


