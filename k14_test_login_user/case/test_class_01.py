# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
import unittest
import time
from page.logingpage import LoginPage,login_url

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome() #只打开一次浏览器
        cls.logindriver=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url) #每次都走登陆页

    # 因为输入账号、密码、登陆是重复动作，只是账号不同，
    # 所以就把重复的过程写成一个方法
    def logintest(self,user,pwd):
         # 1、输入账号
        self.logindriver.input_user(user)
        # 输入密码
        self.logindriver.inut_pwd(pwd)
        # 点击登陆按钮
        self.logindriver.click_button()
        # 获取登陆结果
        result=self.logindriver.get_login_text()
        print result #打印登陆结果
        return result #返回布尔值

    # 用例（实例）可以调用方法，方法不能调用用例
    # 登陆成功案例
    def test_01(self):
        u"""登陆成功案例"""
        # 获取登陆结果
        result=self.logintest("yuele","a12593")
        # 期望结果
        exp=u"首页"
        self.assertEqual(result,exp) #断言

    # 登陆失败案例
    def test_02(self):
        u"""登陆失败案例"""
        # 获取登陆结果
        result=self.logintest("admin","123456")
        # 期望结果
        exp=""
        self.assertNotEqual(result,exp)

    def tearDown(self):
        self.driver.delete_all_cookies() #删除所有的cookie

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit() #关闭浏览器

if __name__=="__main__":
    unittest.main