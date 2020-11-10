# !/usr/bin/python
# coding:utf-8
from common.base import BasePage
from selenium import webdriver
import time
import unittest
# 登陆
login_url="https://club.cy-games.com:9173/"

class LgoinPage(BasePage):
    # 定位需要测试点的元素
    username_loc=("name","username")
    pwd_loc=("name","password")
    button_loc=("css selector",".el-button.el-button--primary.el-button--medium")
    # u_login=("class name","remember-check checkbox-bwxr active")  #x天内免登陆

    # 单个行为封装
    #输入账号
    def input_username(self,user):
        # 调用的BasePage中的send_keys方法,username是需要实例化的，加上self.
        self.send_keys(self.username_loc,user)
    # 输入密码
    def input_pwd(self,pwd):
        self.send_keys(self.pwd_loc,pwd)
    # 点击登陆按钮
    def click_login_button(self):
        self.click(self.button_loc)

    # 是否点击免登陆
    def is_unlogin(self):
        self.click(self.u_login)

    # 封装登陆流程
    def login(self,user="yuele",pwd="a12593"):
        self.input_username(user)
        self.input_pwd(pwd)
        self.click_login_button()
        self.is_login_sucess()

    # 判断是不是登陆成功了
    def is_login_sucess(self):
        try:
            sucess_loc=("css selector",".dashboard-editor-container>h3") #输入登录后用户名字的属性值
            result=self.is_text_in_element(sucess_loc,u"欢迎您回家，尊敬悦乐公会的公会长。")
            return result
        except:
            return False


if __name__=="__main__":
    # 实例化
    driver=webdriver.Firefox() #全局的方法
    login_driver=LgoinPage(driver) #类的方法
    driver.get(login_url)
    login_driver.login()


    # time.sleep(10)
    # driver.quit()
