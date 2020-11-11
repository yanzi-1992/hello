# !/usr/bin/python
# coding:utf-8
import time
print (dir(time))

#返回当前时间是秒数，浮点数
print time.time()
# 返回cup时间，浮点数
time.clock()
# 线程休眠，什么都不用做
time.sleep(1)
# 外国常用
print time.ctime()
# 常用，自定义时间格式
curTime=time.strftime("%Y-%m-%d %H:%M:%S") #年月日时分秒
print curTime

