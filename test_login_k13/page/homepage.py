# !/usr/bin/python
# coding:utf-8
from common.base import BasePage
from selenium import webdriver
import time

# 首页的封装类
# 登陆成功后的首页
home_url="https://club.cy-games.com:9173/#/home"

class HomePage(BasePage):

    bky_loc=("id","hamburger-container")
    

    def click_bky(self):
        self.click(self.bky_loc)
    # 判断图片（logo）是否存在
    def is_exists_img(self):
        img_loc=("css selector",".sidebar-logo")
        result=self.is_exists(img_loc)
        return result

if __name__=="__main__":
    driver=webdriver.Firefox()
    homedriver=HomePage(driver)
    driver.get(home_url)
    homedriver.click_bky()
    result=homedriver.is_exists_img()
    print result

    time.sleep(5)
    driver.quit()