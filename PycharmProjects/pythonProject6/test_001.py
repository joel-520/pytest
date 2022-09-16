"""
命名规则
命令行参数  可以指定 目录、文件名作为存放测试用例的地方
寻找过程会递归到子目录中
  在这些目录中，搜索由其测试包名导入的test——*.py或*_test.py文件
  从这些文件中，搜集如下测试项： test为前缀的 ---函数---   Test为前缀的---类---里面的test为前缀的方法
"""
def add1(x):
    return x+1

def add2(x):
    return x+2


class Testabc:
    def test_add1(self):
        print("测试用例001开始")
        assert add1(3) == 4
        print("测试用例001结束")

    def test_add2(self):
        print("测试用例002开始")
        assert add2(3) == 3
        print("测试用例002结束")
