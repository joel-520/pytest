# 1 导入unittest
import unittest

# 2 创建测试类
class TestDmeo(unittest.TestCase):

    # 3 编写test case
    def test_case_0001(self):
        """测试用例0001"""
        print("执行测试用例0001")

    def test_case_0002(self):
        """测试用例0002"""
        print("执行测试用例0002")

    def test_case_0003(self):
        """测试用例0003"""
        print("执行测试用例0003")


if __name__ == '__main__':
    # 1. 创建测试套件
    suite = unittest.TestSuite()

    # 2. 向测试套件中添加测试用例
    """
    # 2.1 loadTestsFromName
    # 提示：
        name参数是传入文件名，字符串格式
        格式：模块名.测试类名.测试用例名  
    """
    # suite_1 = unittest.TestLoader().loadTestsFromName('test_demo2.TestDmeo.test_case_01')

    """
    # 2.2 loadTestsFromNames
        参数是一个列表，列表中的元素格式同上
    """
    # suite_1 = unittest.TestLoader().loadTestsFromNames(
    #     ['test_demo2.TestDmeo.test_case_01','test_demo2.TestDmeo.test_case_02'])

    """
    # 2.3  loadTestsFromTestCase
        参数一个测试类名
        当前模块直接传如测试类名称即可
    """
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(TestDmeo)

    # 加入套件
    suite.addTest(suite_1)
    # 3. 执行测试套件中的用例
    runner = unittest.TextTestRunner()
    runner.run(suite)