"""
新增学院接口测试--批量新增
"""

# 测试用例是在unittest框架下编写
import unittest
from interface.add_departments import Add_department  # 导入新增学院接口
from common.getKeyword_forResult import GetKeyword  # 返回值处理接口
# 步骤1：导入OperationExcel数据读取脚本和ddt模块
from common.opreationexcel import OperationExcel
import ddt

# 步骤2：对OperationExcel进行实例化
# 获得文件对象
oper = OperationExcel("../data/add_dep.xls")
# 获取数据
test_data = oper.get_data_by_dict()


# 测试添加和查询学院的关联型接口
# 步骤3
@ddt.ddt()
class Test_Add_Dep(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/api/departments/"
        # 实例化Add_department
        self.add_dep = Add_department(self.url)

    # 开始编写测试用例
    # 步骤4
    @ddt.data(*test_data)
    def test_add_dep_success(self, data):  # 步骤5：出入data参数
        """
        测试添加学院成功接口
        :return:
        """
        # 步骤6：准备数据
        req_data = {
            "data": [
                {
                    "dep_id": data["dep_id"],
                    "dep_name": data["dep_name"],
                    "master_name": data["master_name"],
                    "slogan": data["slogan"]
                }
            ]
        }

        # 新增学院
        response = self.add_dep.add_dep(req_data)
        # 获取添加成功后的dep.id

        # 步骤7：完成测试逻辑
        # 如果添加学院参数请求错误，会出现status_code属性
        # 且status_code属性返回400
        if "status_code" in response.keys():
            res = GetKeyword.get_keyword(response, "status_code")
        else:
            # 添加学院成功，则获取添加后学院的id
            """
            # 因为直接使用该方法相当于又执行了一次添加学院接口
            # 所以不能够这样调用
            self.add_dep.get_depid(data)
            """
            res = GetKeyword.get_keyword(response["create_success"], "dep_id")

        # 断言
        self.assertEqual(res, data["expect"])


if __name__ == '__main__':
    unittest.main()
