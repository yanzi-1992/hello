# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
from common.base import BasePage
# 导入所有异常类的包
from selenium.common.exceptions import *

login_url="https://club.cy-games.com:9173/"

class LoginPage(BasePage):
    # 定位需要测试点的元素
    user_loc=("name","username")
    pwd_loc=("name","password")
    button_loc=("css selector",".el-button.el-button--primary.el-button--medium")

    # 输入账号
    def input_user(self,text):
        self.send_keys(self.user_loc,text)
    # 输入密码
    def inut_pwd(self,text):
        self.send_keys(self.pwd_loc,text)
    # 点击登陆
    def click_button(self):
        self.click(self.button_loc)
    # 判断是否登陆成功，获取文本进行比对
    # 定位用户登陆成功后显示的用户名,因这个后台没有，所以使用的是网站上随意的一个参数
    sucess_loc=("css selector",".no-redirect") #输入登录后用户名字的属性值
    def get_login_text(self):
        try:
            t=self.get_text(self.sucess_loc)
            print "登陆成功"
            return t

        except:
            print "登陆失败，元素获取异常，返回"
            return False

# if __name__=="__main__":
#     driver=webdriver.Chrome()
#     logindriver=LoginPage(driver)