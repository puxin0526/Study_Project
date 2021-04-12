import pytest

from calculator import Calculator


@pytest.fixture(scope='class')
def calculate():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")
