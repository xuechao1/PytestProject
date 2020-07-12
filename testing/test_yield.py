#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/12 13:06'


# yield  生成器

def fun():
    for i in range(3):
        print(f"i = {i}")
        yield  # return 同时相当于暂停并且记住 上一次的执行位置
        print("end")


f = fun()
next(f)
next(f)
next(f)
