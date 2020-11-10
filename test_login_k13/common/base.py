# !/usr/bin/python
# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 导入所有异常的包
from selenium.common.exceptions import *
import os
from selenium.webdriver.support.select import Select
# 导入by类
from selenium.webdriver.common.by import By
# 鼠标事件包
from selenium.webdriver.common.action_chains import ActionChains

# 底层公共类
# 底层基类封装# 基于原生selenium框架做了二次封装
class BasePage(object):
    # 全局变量
    def __init__(self,driver):
        #启动浏览器参数化
        self.driver=driver
        # 查找元素时间，如果网页太卡的话可以写成30，单位是秒
        self.timeout=30 #超时时间设置
    def open(self,url):
        # 使用get打开url后，最大化窗口，判断title符合预期
        self.driver.get(url)
        self.driver.maximize_window()
    #     定位单个元素
    def find_element(self,locator):
        # 定位元素，locator是元组类型
        element=WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located(locator))
        return element
    # 定位多个元素，定位一组元素
    def find_elements(self,locator):
        elements=WebDriverWait(self.driver,self.timeout).until(EC.presence_of_all_elements_located(locator))
        return elements
    # 点击操作
    def click(self,locator):
        element=self.find_element(locator)
        element.click()
    # 发送文本，清空后输入,is_clear=True开关，是否先去清空，是否先去clear一下
    def send_keys(self,locator,text):
        element=self.find_element(locator)
        # if is_clear==True:element.claer()
        element.send_keys(text)
    # 判断文本在元素里面，没定位到元素返回False,定位到的时候返回判断结果（布尔值）
    def is_text_in_element(self,locator,text):
        try:
            result=WebDriverWait(self.driver,self.timeout).until(EC.text_to_be_present_in_element(locator,text))
            # print "成功"
            return result
        # except Exception as m:
        #     print ("异常提示：%s"%str(m))
        #     return False
        except:
            # print "失败"
            return False
    # 判断元素value值，没定位到元素返回False,定位到返回判断结果（布尔值）
    def is_text_in_value(self,locator,value):
        try:
            va=WebDriverWait(self.driver,self.timeout).until(EC.text_to_be_present_in_element_value(locator,value))
            return va
        except:
            return False
    # 判断title完全等于
    def is_title(self,title):
        try:
            result=WebDriverWait(self.driver,self.timeout).until(EC.title_is(title))
            return result
        except:
            return False
    # 判断title包含
    def is_title_contains(self,title):
        try:
            result=WebDriverWait(self.driver,self.timeout).until(EC.title_contains(title))
            return result
        except:
            return False
    # 判断元素被选中，返回布尔值 ，只针对有下拉框的，并不是所有都是用
    def is_selected(self,locator):
        try:
            result=WebDriverWait(self.driver,self.timeout).until(EC.element_located_selection_state_to_be(locator))
            return result
        except:
            return False
    # 判断页面是否alert,有返回alert（注意这里返回的是alert,不是True），没有返回False
    def is_alert_present(self):
        try:
            alert=WebDriverWait(self.driver,self.timeout).until(EC.alert_is_present())
            return alert
        except:
            return False
    # 判断元素被定位到（并不意味可见），定位到了返回elemet,没定位到返回false
    def is_located(self,locator):
        try:
            result=WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located)
            return result
        except:
            return False
    # 判断元素是否存在
    def is_exists(self,locator):
        try:
            self.is_exists(locator)
            return True
        except:
            return False
    # 判断iframe是否可以切入，locator是tuple类型，locator也可以是id和name名称，返回布尔值
    def is_iframe(self,locator):
        try:
            result=WebDriverWait(self.driver,self.timeout).\
                until(EC.frame_to_be_available_and_switch_to_it(locator))
            return result
        except:
            return False
    # 鼠标悬停操作
    def move_to_element(self,locator):
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    # 获取title
    def get_titile(self):
        return self.driver.title
    # 获取文本
    def get_text(self,locator):
        t=self.find_element(locator).text
        return t
    # 获取元素属性
    def get_attribute(self,locator,name):
        element=self.find_element(locator)
        return element.get_attribute(name)
    # 通过索引，index是所以第几个，从0开始，默认选第一个
    def selcet_by_index(self,locator,index=0):
        element=self.find_element(locator)
        Select(element).select_by_index(index)
        element.click()
    # 获取当前的句柄
    def get_current_handle(self):
        return self.driver.current_window_handle
    # 获取所有的句柄
    def get_handles(self):
        time.sleep(1)
        h=self.driver.window_handles #获取所有的句柄
        if len(h)<=1:
            print "当前只获取到一个窗口句柄，等待3秒之后重新获取"
            time.sleep(3)
            h=self.driver.window_handles
        return h

# if __name__=="__main__":
#     driver=webdriver.Firefox()
#     my_driver=BasePage(driver)
#     my_driver.open("http://www.baidu.com")
#
#     # 鼠标悬停时间
#     shezhi_loc=("id","s-usersetting-top")
#     my_driver.move_to_element(shezhi_loc)
#     # 获取元素属性
#     d=my_driver.get_attribute(shezhi_loc,"name")
#     print d
#
#     # 定位一组元素
#     # loc=("class name","mnav") #先定义抓取元素方法
#     # elements=my_driver.find_elements(loc) #接受元组类型参数
#     # print len(elements)
#     # # print type(elements) #打印数据类型
#     # # 用复数定位的方法点击第1个元素（使用下标）
#     # elements[0].click()
#
#     # 休眠然后关闭
#     time.sleep(10)
#     driver.quit()
