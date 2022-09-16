"""
1.学习目标
    掌握unittest框架下测试用例编写方法
2.操作步骤
    2.1 导入unittest
    2.2 创建测试类
        测试类名称需要Test开头
        继承unittest中的TestCase基本类
        class Test_demo(unittest.TestCase):
    2.3 编写test fixture
        setUp()--前置函数
        tearDown()--后置函数
        setUpClass()--+@classmethod
        tearDownClass()+@classmethod
    2.4 编写test case
        测试方法名称均以test开头
        测试用例执行顺序:按照测试用例名称ASCII字符集编码排序。
        所以我们在执行测试类中的测试方法的时候，要注意测试方法的执行顺序。
3.需求
    编写简单的测试类
"""
# 1 导入unittest
import unittest


# 2 创建测试类
class Test_demo(unittest.TestCase):
    # 3 编写test fixture
    # setUp我们也称之为前置函数
    def setUp(self) -> None:
        print("setUp在每个测试用例执行前先执行。")

    # setUp我们也称之为后置函数
    def tearDown(self) -> None:
        print("tearDown在每个测试用例执行后执行。")

    @classmethod
    # cls等同于self，用于函数和类方便区分。
    def setUpClass(cls) -> None:
        print("setUpClass在测试类执行前先执行。")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass在测试类执行后执行。")

    # 4 编写test case
    # 每个测试方法均以test开头，否则是不被unittest识别的。
    def test_case_03(self):
        """测试用例3，这里是测试用例的备注"""
        # 测试方法中，将多行注释写在第一行，就是该方法的备注。
        print("执行测试用例3")

    def test_case_02(self):
        """测试用例2"""
        print("执行测试用例2")

    def test_case_01(self):
        """测试用例1"""
        print("执行测试用例1")


if __name__ == '__main__':
    # 执行当前测试类中，以test开头的所有测试用例
    unittest.main()


"""
输出结果：
setUpClass在测试类执行前先执行。
setUp在每个测试用例执行前先执行。
执行测试用例1
tearDown在每个测试用例执行后执行。
setUp在每个测试用例执行前先执行。
执行测试用例2
tearDown在每个测试用例执行后执行。
setUp在每个测试用例执行前先执行。
执行测试用例3
tearDown在每个测试用例执行后执行。
tearDownClass在测试类执行后执行。
"""