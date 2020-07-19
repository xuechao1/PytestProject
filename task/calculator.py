#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/18 17:55'

import random

# 计算器
ran_number = random.randint(1, 100)
while True:
    input_number = int(input("请输入一个数字\n"))
    if input_number > ran_number:
        print("小一点")
    elif input_number < ran_number:
        print("大一点")
    elif input_number == ran_number:
        print("猜对了")
        break
