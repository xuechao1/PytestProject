#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/12 12:04'

import sys

print(sys.path.append('..'))
import pytest
from pythoncode.calc import Calcuator


# 模块级别
def setup_module():
    print("模块级别   setup")


def teardown_module():
    print("模块级别   teardown")


# 函数级别  类外面的使用def 定义的叫做函数，
# 在类里面使用def 定义的叫方法
def setup_function():
    print("函数级别  setup")


def teardown_function():
    print("函数级别   teardown")


def test_case1():
    print("testcase1")


class TestCalc:
    # setup_class，teardown_class 每个类里面，执行前后 分别执行
    def setup_class(self):
        self.cal = Calcuator()
        print("类级别  setup")

    def teardown_class(self):
        print("类级别  teardown")

    # 方法级别  每条类里面的测试用例前和后分别  执行setup teardowm
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 2),
        (2, 2, 4),
        (200, 200, 400),
        (0.2, 0.2, 0.4),
    ], ids=['int', 'int', 'bignum', 'float'])
    def test_add(self, a, b, result):
        # cal = Calcuator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add2(self):
        # cal = Calcuator()
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.div
    def test_div(self):
        # cal = Calcuator()
        assert 1 == self.cal.div(1, 1)
