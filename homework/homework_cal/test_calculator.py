# 测试计算器功能
import allure
import pytest
import yaml

from calculator import Calculator


def get_datas():
    with open('./calculator_datas.yml') as f:
        datas = yaml.safe_load(f)
        return datas


@allure.feature('计算器加减乘除测试')
class TestCal:
    @allure.story('加法')
    # 测试加法(整数）
    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'])
    def test_add_int(self, calculate, a, b, expect):
        assert calculate.add(a, b) == expect

    @allure.story('加法')
    # 测试加法(浮点数）
    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'])
    def test_add_float(self, calculate, a, b, expect):
        assert round(calculate.add(a, b), 2) == expect

    @allure.story('减法')
    # 测试减法(整数）
    @pytest.mark.parametrize('a,b,expect', get_datas()['sub_int']['datas'])
    def test_sub_int(self, calculate, a, b, expect):
        assert calculate.sub(a, b) == expect

    @allure.story('减法')
    # 测试减法(浮点数）
    @pytest.mark.parametrize('a,b,expect', get_datas()['sub_float']['datas'])
    def test_sub_float(self, calculate, a, b, expect):
        assert round(calculate.sub(a, b), 2) == expect

    @allure.story('乘法')
    # 测试乘法(整数）
    @pytest.mark.parametrize('a,b,expect', get_datas()['mul_int']['datas'])
    def test_mul_int(self, calculate, a, b, expect):
        assert calculate.mul(a, b) == expect

    @allure.story('乘法')
    # 测试乘法(浮点数）
    @pytest.mark.parametrize('a,b,expect', get_datas()['mul_float']['datas'])
    def test_mul_float(self, calculate, a, b, expect):
        assert round(calculate.mul(a, b), 2) == expect

    @allure.story('除法')
    # 测试除法
    @pytest.mark.parametrize('a,b,expect', get_datas()['div_int']['datas'])
    def test_div_int(self, calculate, a, b, expect):
        try:
            assert round(calculate.div(a, b), 2) == expect
        except ZeroDivisionError:
            assert expect == 'error'
