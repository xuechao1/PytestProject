#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/19 19:14'

import pytest


def test_success():
    assert True


def test_failure():
    assert False


def test_skip():
    pytest.skip("for one reason")


def test_broken():
    raise Exception('oops')
