#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/12 13:18'

import pytest


# scope='session'   每个项目只执行一次，整个python执行一次
# scope='module'    每个模块也就是每个.py文件，只执行一次
# @pytest.fixture(scope='session')  # 实现在 单个方法里面执行 setup_class
# @pytest.fixture(autouse=True, params=['user1', 'user2', 'user3'])
@pytest.fixture(params=['user1', 'user2', 'user3'])
def login(request):
    print("登录方法")
    print(request.param)
    # yield  激活fixture teardown方法
    yield ['username', 'password']
    print("teardowm")
