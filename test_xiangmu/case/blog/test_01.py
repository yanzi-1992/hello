# !/usr/bin/python
# coding:utf-8
import unittest
from selenium import webdriver
import time

class Test1(unittest.TestCase): #测试套件 TestSuite
    u"""百度用例"""
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.baidu")
    # 要截图的话，一定要定义driver参数，并且设置全局self
    def test_01(self): #测试用例 TestCase
        """百度首页标题用例"""
        t=self.driver.title
        print (u"首页标题"+t)
        q=u"百度一下，你就知道"
        self.assertEqual(t,q)
    def test_02(self):
        u"""百度输入框"""
        self.driver.find_element_by_id("kw").send_keys("123")
        b=self.driver.title
        print (b)
        p=u"123"
        self.assertEqual(b,p)
        # self.assertNotEqual(b,p)
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    if __name__=="__mian__":
        unittest.man
