# !/usr/bin/python
# coding:utf-8


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()
# login_url="https://passport.bilibili.com/login"
login_url="https://club.cy-games.com:9173/"
driver.get(login_url)
# locator =username_loc=("id","login-username")
# pwd_loc=("id","login-passwd")
# button_loc=("class name","btn btn-login")
# u_login=("class name","remember-check checkbox-bwxr active")

# WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))

# driver.find_element_by_id("login-username").send_keys("123")
# driver.find_element_by_id("login-passwd").send_keys("456")
driver.find_element_by_name("username").send_keys("yuele")
driver.find_element_by_name("password").send_keys("a12593")
driver.find_element_by_css_selector(".el-button.el-button--primary.el-button--medium").click()
driver.find_element_by_id("hamburger-container").click()
# driver.find_element_by_link_text(u"新闻").click()
# driver.find_element_by_name("tj_login").click()

time.sleep(10)
driver.quit()