# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
import os
import base64
# 邮箱需要用的包
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(smtpsever,port,sender,pwd,receiver,fp):
    try:
        # 邮件模板
        msg=MIMEMultipart() #邮件内容
        msg['Subject']="这是一份测试邮件" #邮件标题，主题
        msg['From']=sender #发送者
        msg['To']=receiver #接收者

        #读取文件
        f=open(fp)
        # print f
        mail_body=f.read()
        f.close()
        # 添加附件到容器
        att = MIMEText(mail_body,"base64", "utf-8") #传送这个文件
        att["Content-Type"] = "application/octet-stream"
        #filename= “测试结果的文件",这里可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename= "result.html"'
        msg.attach(att) #添加附件
        # 加正文
        body=MIMEText(mail_body,"html", "utf-8")
        msg.attach(body)

        #  写信流程
        smtp=smtplib.SMTP_SSL(smtpsever,port) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是465
        smtp.login(sender,pwd) # 发送者的邮箱账号，密码(授权码)
        smtp.sendmail(sender,receiver,msg.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        smtp.quit()#发送完了之后退出smtp
        print "邮件发送成功"
        return True
    except Exception as m:
        print ("异常提示：%s"%str(m))
        return False
    except:
        print "邮件发送失败"
        return False

# 断言是否发送成功
# 方法1、函数没有形参的时候
# assert send_email()==True
# 方法2、函数有形参的时候
# if __name__=="__main__":
#     smtpsever="smtp.qq.com"          #发件服务器
#     port=465                         #端口
#     sender="1272974445@qq.com"      #发件人
#     pwd="iqluqbkudkmogbda"          #密码
#     receiver="836442389@163.com"  #收件人
#     fp="E:\\test_xiangmu\\report\\result.html"   #邮件正文
# 断言，看邮件是否发送成功
# assert send_email(smtpsever,port,sender,pwd,receiver,fp)==True