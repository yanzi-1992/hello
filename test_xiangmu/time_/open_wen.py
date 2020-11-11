# !/usr/bin/python
# coding:utf-8

d="E:\\csv.txt"

# r 读取某个文件
fp=open("E:\\csv.txt","r")
r=fp.read()
print r
fp.close()

# w 往文件中写入,先清空之前的数据写入新数据
fp=open("E:\\csv.txt","w")
# w=fp.write("11,22,33,44,xieru")
fp.close()

# a 追加写入，不清空之前的数据，接着后面写入新数据
fp=open(d,"a")
z=fp.write("\nzhujia")
fp.close()

# wb 写文件,创建一个文件并且写入数据
fp=open("E:\\web.txt","wb")
w=fp.write("123")
fp.close()