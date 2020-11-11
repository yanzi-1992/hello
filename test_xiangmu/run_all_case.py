# !/usr/bin/python
# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
# from common import HTMLTestRunner
import HTMLTestRunner
import time


# 测试用例的文件位置
# start_dir="E:\\test_xiangmu\\case"

discover=unittest.defaultTestLoader.discover(start_dir="E:\\test_xiangmu\\case",
                                             pattern="test*.py",top_level_dir=None)
# 确认一下是否加载到测试用例
print (discover)

# 执行用例，生成文本的报告
# runner=unittest.TextTestRunner() #返回实例,运行器
# runner.run(discover) #运行

#存放测试报告的位置
reportPath="E:\\test_xiangmu\\report\\"+"result.html"
print (reportPath)

# wb是写入文件的意思
fp=open(reportPath,"wb")
# verbosity=1 是不显示注释的意思
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                     verbosity=2,
                                     title=u"这个是我的自动化报告",
                                     description=u"这个是项目的用例执行情况：")
runner.run(discover)
