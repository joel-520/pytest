# coding=utf-8
import time
import os
import unittest
import HTMLTestRunner

# 定位测试用例目录(可以再封装)
project_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
testcase_dir = project_dir + r"\testcase"


def creatsuite():
    '''获取测试集'''
    # 搜索测试用例
    testcases = unittest.defaultTestLoader.discover(testcase_dir, pattern="test*.py", top_level_dir=None)
    return testcases


def run(title=u'自动化测试报告', description=u'环境配置等信息'):
    """执行测试并生成报告"""

    # 如果没有测试报告目录自动创建
    for filename in os.listdir(project_dir):
        if filename == "reports":
            break
    else:
        os.mkdir(project_dir + r'\reports')

    # 执行测试用例并生成测试报告
    # 1 确定测试报告存放路径
    report_path = project_dir + r'\reports'
    print(report_path)
    # 2 确定测试报告名称
    now = time.strftime("%Y_%m_%d_%H-%M-%S")
    report_file = report_path + "\\" + now + "report.html"  # 测试报告文件名

    # 打开文件并写入
    with open(report_file, "wb") as fp:
        # 实例化
        """
            title：报告的标题
            description：报告的描述
            stream:执行结果全部卸载该文件纵
            verbosity：报告的详细程度，0.1.2 ，2为最详细
            retry：重试，这个是坏的，不能用
        """
        runner = HTMLTestRunner.HTMLTestRunner(
            title=title,
            description=description,
            verbosity=2,
            stream=fp
        )
        runner.run(creatsuite())


if __name__ == '__main__':
    run()
    """
    封装成目录，如果需要生成报告的测试，
    直接调用该模块中的run()方法即可。

    例如：
        # 引入模块
        from util import TestRunnerReport

        # 执行测试用例
        TestRunnerReport.run(title='ewr',description='123131')

    注意：这里只是提供一种封装的思路，仅供参考，
        可以根据自己的情况按需封装。
    """