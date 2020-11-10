# !/usr/bin/python
# coding:utf-8
import ddt
from page.logingpage import LoginPage,login_url
from selenium import webdriver
import unittest
import time
# ddt数据驱动
data=[
    {"user":"yuele","pwd":"a12593","exp":u"首页"},
    {"user":"admin","pwd":"123456","exp":"123"}
]
#测试类前面：@ddt.ddt
@ddt.ddt
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
    # 测试用例前：@ddt.data
    @ddt.data(*data)
    def test_01(self,testdata):
        print testdata
        u"""登陆成功案例""" #ddt坏处：注释不会都写出来，没办法知道每个测试用例的注释是什么
        try:
            # 获取登陆结果
            result=self.logintest(**testdata)
            #ddt 好处：写好方法，写好参数，可直接调用出来
            # 期望结果
            self.assertTrue(result) #断言
            print "---登陆成功---"
            return True
        except:
            print "---登陆失败---"
            return False

    def tearDown(self):
        self.driver.delete_all_cookies() #删除所有的cookie

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit() #关闭浏览器

if __name__=="__main__":
    unittest.main