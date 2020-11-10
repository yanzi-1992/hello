# !/usr/bin/python
# coding:utf-8
from page.loginpage import LgoinPage,login_url
from page.homepage import HomePage,home_url
import unittest
from selenium import webdriver

class HomeTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.logindriver=LgoinPage(self.driver) #登陆页面
        self.homedriver=HomePage(self.driver) #首页主页
        # 先登录
        self.driver.get(login_url)
        # 执行登陆结果
        self.logindriver.login()

    def test_click_bky(self):
        # 打开首页
        self.driver.get(home_url)
        self.homedriver.click_bky() #点击首页某个按钮
        # 判断结果
        result=self.homedriver.is_exists_img()
        print result #打印返回结果是否为真
        # 断言
        self.assertTrue(result)