# !/usr/bin/python
# coding:utf-8
import unittest
from selenium import webdriver
from page.loginpage import LgoinPage,login_url

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.logindrvier=LgoinPage(self.driver)
        self.driver.get(login_url)

    def test_01(self):
        try:
            # 1、输入账号
            self.logindrvier.input_username("yuele")
            # 2、输入密码
            self.logindrvier.input_pwd("a12593")
            # 3、点击登陆按钮
            self.logindrvier.click_login_button()
            # 4、获取登陆结果
            result=self.logindrvier.is_login_sucess()
            # 5、断言
            self.assertTrue(result)
            print "登陆成功"
            return True
        except:
            print "登陆失败"
            return False

if __name__=="__main":
    unittest.main