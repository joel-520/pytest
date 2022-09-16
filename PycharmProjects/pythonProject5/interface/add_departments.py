"""
测试新增和查询接口(组合接口业务)
    先新增--->再查询
"""
# 测试用例是在unittest框架下编写
import unittest
from interface.add_departments import Add_department  # 导入新增学院接口
from interface.get_departments import Get_Departments  # 查询学院接口
from common.getKeyword_forResult import GetKeyword  # 返回值处理接口


# 测试添加和查询学院的关联型接口
class Test_Add_Get_Dep(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        # 实例化Add_department添加学院
        self.add_dep = Add_department(self.url)
        # 实例化Get_Departments查询学院
        self.get_dep = Get_Departments(self.url)

    # 开始编写测试用例
    def test_add_get(self):
        # 封装请求参数
        add_data = {
            "data": [
                {
                    "dep_id": "T03",
                    "dep_name": "Test学院",
                    "master_name": "Test-Master",
                    "slogan": "Here is Slogan"
                }
            ]
        }

        # 一下逻辑待查证，知道组合的形式即可。
        # 执行添加学院接口。目的：获取添加成功后的学院id
        # 获取新增学院后的id
        dep_id = self.add_dep.get_keyword(add_data, "dep_id")
        # 查询新增学院信息
        result = self.get_dep.get_department(dep_id)
        # 通过获取查询后的学院id作为实际结果
        res_dep_id = GetKeyword.get_keyword(result, "dep_id")
        # 获取预期结果id
        expect = GetKeyword.get_keyword(add_data, "dep_id")
        # 断言结果
        self.assertEqual(expect, res_dep_id)


if __name__ == '__main__':
    unittest.main()

