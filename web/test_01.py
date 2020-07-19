#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/14 23:40'

import time
from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get('https://work.weixin.qq.com/')
driver.maximize_window()
# driver.implicitly_wait(5)
time.sleep(3)
driver.quit()
