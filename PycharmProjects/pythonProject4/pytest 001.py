import pytest

def test_01():
    print("this is test 01")
    assert 1 == 1
def test_02():
    print("this is test 02")
    assert 2 == 3

if __name__ == '__main__':
    pytest.main(['pytest 001.py'])