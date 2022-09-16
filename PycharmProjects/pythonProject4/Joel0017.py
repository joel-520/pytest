#用例标题和用例描述定制详解
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 上午10:10
# @Author  : WangJuan
# @File    : test_case.py
import allure
import pytest

@allure.feature('test_module_01')
@allure.story('test_story_01')
#test_case_01为用例title
def test_case_01():
    """
    用例描述：这是用例描述，Test case 01，描述本人
    """
    #注释为用例描述
    assert 0

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
