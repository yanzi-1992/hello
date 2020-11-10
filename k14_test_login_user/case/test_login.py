# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
import unittest
import time
from page.logingpage import LoginPage,login_url

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.logindriver=LoginPage(self.driver)
        self.driver.get(login_url)
    # 登陆成功
    def test_01(self):
        # 1、输入账号
        self.logindriver.input_user("yuele")
        # 输入密码
        self.logindriver.inut_pwd("a12593")
        # 点击登陆按钮
        self.logindriver.click_button()
        # 获取登陆结果
        result=self.logindriver.get_login_text()
        # 期望结果
        exp=u"首页"
        self.assertEqual(result,exp) #assertEqual（a,b）验证a=b
    # 登陆失败
    def test_02(self):
        # 1、输入账号
        self.logindriver.input_user("admin")
        # 输入密码
        self.logindriver.inut_pwd("123456")
        # 点击登陆按钮
        self.logindriver.click_button()
        # 获取登陆结果
        result=self.logindriver.get_login_text()
        # 期望结果
        exp=""
        self.assertNotEqual(result,exp) #assertNotEqual（a,b）验证a!=b，不等于

if __name__=="__main__":
    unittest.main