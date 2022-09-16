# content of test_joel002.py

import pytest

@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app

def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        pass

if __name__ == "__main__":
    pytest.main(["-s", "test_joel002.py", "-m=not webtest"])

'''只运行用webtest标记的测试，cmd运行的时候，加个-m 参数，指定参数值webtest

```py
pytest -v -m webtest'''