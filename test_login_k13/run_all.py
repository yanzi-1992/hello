# !/usr/bin/python
# coding:utf-8
# 2.7版本解决乱码用的
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
from selenium import webdriver
# 导入邮箱需要的3个包
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 导入路径需要包
import os
#导入公共方法的包
from common import HTMLTestRunner

# 第一步加载测试用例
# 第二步执行测试用例
# 第三步获取最新测试报告
# 第四步发送邮箱

#当前文件的真实路径
cur_path=os.path.dirname(os.path.realpath(__file__))

