# -*- coding: utf-8 -*-
# @Time : 2022/9/16 12:59
# @Author : joel
# @Email : 770546904@qq.com
# @Filename: commons/assert_util
# @Describe: ...
import jsonpath


def assert_result(validate,res):
    for key, value in validate.items():
        if key == 'codes':
            codes_assert(value,res.status_code)
        if key == 'equals':
            equals_assert(value,res.json())
        if key == 'conntains':
            contains_assert(value,res.text)
        if key == 'databases':
            db_assert(value,res.json())
        else:
            print("不支持的断言方式")


#  #异常断言
# def raise_assert_error(msg):
#     raise AssertionError(msg)


#状态码断言
def codes_assert(yq_value,sj_value):
    if yq_value != sj_value:
        raise AssertionError("codes 断言失败！预期结果："+str(yq_value)+" ,实际结果："+str(sj_value)+"")

#相等断言
def equals_assert(yq_value,sj_json_value):
    for key,value in yq_value.items():
        lists = jsonpath.jsonpath(sj_json_value, "$..%s" % key)
        if lists:
            if value not in lists:
                raise AssertionError("equals_assert断言失败！"+str(yq_value)+"不等于"+str(sj_json_value)+"")
        else:
            raise AssertionError("equals_assert断言失败！返回结果没有"+str(key)+"")

#包含断言
def contains_assert(yq_value,sj_text_value):
    if str(yq_value) not in sj_text_value:
        raise AssertionError("contains 断言失败！预期结果没有"+str(yq_value)+"")


# 数据库断言
def db_assert(yq_value,sj_json_value):
    for key,sql in yq_value.items():
        list_result = jsonpath.jsonpath(sj_json_value,"$..%s" % key)
        if list_result:
            try:
                select_result = execute_sql(sql)
            except:
                raise AssertionError("database断言失败：SQL查询异常")

            else:
                if len(select_result) ==0:
                    raise AssertionError("database断言失败：SQL查询没有结果返回")
                else:
                    print("SQL查询到值")
                    print("list_result: %s" % list_result)
                    print("select_result: %s" % select_result)
                    if list_result[0] not in select_result:
                        raise AssertionError("dbbases 断言失败！预期结果" + str(list_result[0]) + "不等于实际结果" + str(select_result[0]) + "")
        else:
            raise AssertionError("dbbases 断言失败！返回结果中没有" + str(key) + "")







