import pytest
@pytest.mark.run(order=1)
def test_01():
    print('test01')

@pytest.mark.run(order=2)
def test_02():
    print('test01')
@pytest.mark.last
def test_06():
    print('test01')

def test_04():
    print('test01')

def test_05():
    print('test01')
@pytest.mark.run(order=3)
def test_03():
    print('test01')

pytest_order.py::test_01 PASSED [ 16%]test01

pytest_order.py::test_02 PASSED [ 33%]test01

pytest_order.py::test_03 PASSED [ 50%]test01

pytest_order.py::test_04 PASSED [ 66%]test01

pytest_order.py::test_05 PASSED [ 83%]test01

pytest_order.py::test_06 PASSED [100%]test01
