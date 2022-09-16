#固件
import pytest



@pytest.fixture(scope="function",autouse=False,params=[{"name":"百里"},{"name":"beifam"}],name="sql")
def exe_sql(request):
    print("aaaa")
    yield request.param
    print("aaa")