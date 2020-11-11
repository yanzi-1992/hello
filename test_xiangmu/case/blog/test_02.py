# !/usr/bin/python
# coding:utf-8
import unittest
from selenium import webdriver
import time

class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print (u"--我是登陆--")

    def test_03(self):

        print (u"我是03")

    def test_04(self):
        u'''测试用例04'''
        print (u"我是04")

    @classmethod
    def tearDownClass(cls):
        print (u"我是退出")

    if __name__=="__mian__":
        unittest.main