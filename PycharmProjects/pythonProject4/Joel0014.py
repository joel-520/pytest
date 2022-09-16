# web_conf_py/conftest.py
import pytest

@pytest.fixture(scope="session")
def start():
    print("\n打开首页")
    return "yoyo"

# web_conf_py/baidu/conftest.py
import pytest

@pytest.fixture(scope="session")
def open_baidu():
    print("打开百度页面_session")

# web_conf_py/baidu/test_1_baidu.py
import pytest
import time

def test_01(start, open_baidu):
    print("测试用例test_01")
    time.sleep(1)
    assert start == "yoyo"

def test_02(start, open_baidu):
    print("测试用例test_02")
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_1_baidu.py"])


# web_conf_py/baidu/test_2.py
import pytest
import time

def test_06(start, open_baidu):
    print("测试用例test_01")
    time.sleep(1)
    assert start == "yoyo"
def test_07(start, open_baidu):
    print("测试用例test_02")
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_2.py"])


# web_conf_py/blog/conftest.py
import pytest

@pytest.fixture(scope="function")
def open_blog():
    print("打开blog页面_function")

# web_conf_py/blog/test_2_blog.py

import pytest
import time
def test_03(start, open_blog):
    print("测试用例test_03")
    time.sleep(1)
    assert start == "yoyo"

def test_04(start, open_blog):
    print("测试用例test_04")
    time.sleep(1)
    assert start == "yoyo"

def test_05(start, open_blog):
    '''跨模块调用baidu模块下的conftest'''
    print("测试用例test_05,跨模块调用baidu")
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_2_blog.py"])
