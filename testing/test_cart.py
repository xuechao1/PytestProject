#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/12 13:27'

import pytest


def test_cart1(login):
    print("购物车用例1")


def test_cart2(login):
    print("购物车用例2")


@pytest.fixture()
def fun1():
    print("这是另一个fixture1")


# 参数化结合 fixture 使用
# 情况一：传入值 和 数据
# 情况二：传入一个fixture方法，将数据传入fixture方法中
#           fixture方法使用request参数来接收这组数据，在方法体里面使用
#           '''request.param''' 来使用整个数据

@pytest.mark.parametrize('login', [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
def test_cart3(login):
    print("购物车用例3")
