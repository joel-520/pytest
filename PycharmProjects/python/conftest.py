import pytest


@pytest.fixture(scope="function",autouse="true",params=[{"name":"baili"},{"name":"beifan"}],name="sql")
def exe_sql(request):
    print("执行SQL")
    yield request.param
    print("关闭数据库连接")