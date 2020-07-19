#!/usr/bin/env python
# -*- encoding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/19 15:36'

import time
from selenium import webdriver


class CompanyWeixin:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("'https://work.weixin.qq.com/'")
        self.driver.implicitly_wait(5)

    def first_page(self):
        """
        首页PO
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        time.sleep(1)
        self.driver.find_element_by_id('username').send_keys("tester")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("tester")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("tester")
        self.driver.find_element_by_name("mobile").send_keys('14787184017')
        self.driver.find_element_by_xpath('//*[@id="js_contacts40"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        time.sleep(1)
        pass

    def contact_book(self):
        """
        通讯录PO
        :return:
        """
        pass

    def app_manage(self):
        """
        应用管理PO
        :return:
        """
        pass

    def customer_manage(self):
        """
        客户管理PO
        :return:
        """
        pass

    def manage_tool(self):
        """
        管理工具PO
        :return:
        """
        pass

    def my_company(self):
        """
        我的企业PO
        :return:
        """
        pass
