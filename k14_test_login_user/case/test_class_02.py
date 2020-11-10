# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
import unittest
import time
from page.logingpage import LoginPage,login_url

# 数据分离，测试账号(方法2、方法3的调用数据)
test_data1={"user":"yuele","pwd":"a12593","exp":u"首页"}
test_data2={"user":"admin","pwd":"","exp":""}

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome() #只打开一次浏览器
        cls.logindriver=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url) #每次都走登陆页

    # 因为输入账号、密码、登陆是重复动作，只是账号不同，
    # 所以就把重复的过程写成一个方法
    # 把期望结果参数写入方法
    def logintest(self,user,pwd,exp):
         # 1、输入账号
        self.logindriver.input_user(user)
        # 输入密码
        self.logindriver.inut_pwd(pwd)
        # 点击登陆按钮
        self.logindriver.click_button()
        # 获取登陆结果
        result=self.logindriver.get_login_text()
        print result #打印登陆结果
        return result==exp #返回布尔值

    # 用例（实例）可以调用方法，方法不能调用用例
    # 登陆成功案例
    def test_01(self):
        u"""登陆成功案例"""
        # 获取登陆结果
        # 方法1
        # result=self.logintest("yuele","a12593",u"欢迎您回家，尊敬悦乐公会的公会长。")
        # 方法2
        # result=self.logintest(test_data1["user"],test_data1["pwd"],test_data1["exp"])
        # 方法3
        result=self.logintest(**test_data1)
        # 期望结果
        self.assertTrue(result) #断言

    # 登陆失败案例
    def test_02(self):
        u"""登陆失败案例"""
        # 获取登陆结果
        # result=self.logintest("admin","123456",u"欢迎您回家，尊敬悦乐公会的公会长。")
        # result=self.logintest(test_data2["user"],test_data2["pwd"],test_data2["exp"])
        result=self.logintest(**test_data2)
        self.assertFalse(result) #断言

    def tearDown(self):
        self.driver.delete_all_cookies() #删除所有的cookie

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit() #关闭浏览器

if __name__=="__main__":
    unittest.main