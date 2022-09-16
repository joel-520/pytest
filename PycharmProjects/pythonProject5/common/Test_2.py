"""
1.学习目标
    必须掌握unittest中断言使用
2.语法
    2.1 编写位置
            在测试用例中去编写，先执行测试用例，最后一行断言。
    2.2 使用的断言方法
    	注意：前边a是预期，后边b是测试实际的值
        （1）assertEqual(a,b,msg)
            断言a和b是否相等,如果相等,断言成功,否则断言失败
        （2）assertTrue(x,msg)
            断言条件x是否为True,如果是,断言成功,否则断言失败
        （3）其他断言用法类似。
    2.3 判定断言结果
        断言成功,控制台没有任何提示
        断言失败,控制台AssertionError关键字会出现
3.需求
    编写一个有断言的测试类
"""
# 1 导入unittest
import unittest


# 2 创建测试类
class Test_demo(unittest.TestCase):

    # 3 编写test case
    def test_case_03(self):
        """测试用例3"""
        print("执行测试用例3")
        # 用例步骤执行完成后做断言
        # assertEqual断言a和b是否相等
        self.assertEqual(2, 1 + 1, msg="断言成功")

    """
    执行结果：
        断言成功,控制台没有任何提示

    下面是总测试结果的日志：
        执行测试用例3
        # 在0.005秒内进行1次测试
        Ran 1 test in 0.005s

        # 测试用例全部通过
        OK
    """

    def test_case_02(self):
        """测试用例2"""
        print("执行测试用例2")
        # assertEqual断言a和b是否相等
        self.assertEqual(3, 1 + 1, msg="断言失败")

        """
        执行结果：

            执行测试用例2

            断言失败
            3 != 2

            Expected(预期) :2
            Actual(实际)   :3

            下面会有报错信息（主要内容）：
                AssertionError: 2 != 3 : 断言失败

                # 在0.008秒内进行1次测试
                Ran 1 test in 0.008s

                # 失败一个测试用例
                FAILED (failures=1)

                # 断言失败
                Assertion failed
        """

    def test_case_01(self):
        """测试用例1"""
        print("执行测试用例1")
        # 断言条件x是否为True
        self.assertTrue(1 > 2, msg="条件不成立,断言失败")


# 4 编写普通方法
if __name__ == '__main__':
    # 执行当前测试类中，以test开头的测试用例
    unittest.main()