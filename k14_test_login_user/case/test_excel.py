# !/usr/bin/python
# coding:utf-8
from page.logingpage import LoginPage,login_url
from selenium import webdriver
import unittest
import time
import ddt
import xlrd
from common.readExcel import ExcelUtil

d=ExcelUtil("test.xls")
# print d.dict_data() #检查是否读取成功
data=d.dict_data() #读取数据
# print data

#测试类前面：@ddt.ddt
@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome() #只打开一次浏览器
        cls.logindriver=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url) #每次都走登陆页

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

    # 测试用例前：@ddt.data
    @ddt.data(*data)
    def test_01(self,testdata):
        # print testdata
        # 获取登陆结果
        try:
            result=self.logintest(**testdata)
            self.assertTrue(result) #断言
            print "---登陆成功---"
            return True
        except:
            print "---登陆失败---"
            return False

    def tearDown(self):
        time.sleep(5)
        self.driver.delete_all_cookies() #删除所有的cookie

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit() #关闭浏览器

if __name__=="__main__":
    unittest.main



