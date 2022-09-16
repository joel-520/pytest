from urllib import request

import pytest



@pytest.fixture(scope='package',autouse=True)
def st_clearAll():
    print(f'\n---初始化---::构建空白数据环境')

    def fin():
        print(f'\n---清除数据---::构建空白数据环境')

    request.addfinalizer(fin)
