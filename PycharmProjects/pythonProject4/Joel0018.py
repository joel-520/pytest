# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 上午10:10
# @Author  : WangJuan
# @File    : test_case.py
import allure
import pytest
""""
Severity定制详解
Allure中对严重级别的定义：
1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
2、 Critical级别：临界缺陷（ 功能点缺失）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
"""

@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('critical')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('normal')
def test_case_03():
    """
    用例描述：Test case 03
    """
    assert 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('minor')
def test_case_04():
    """
    用例描述：Test case 04
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
