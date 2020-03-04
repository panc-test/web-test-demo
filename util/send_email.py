'''
封装发送邮件操作
'''
import os
import time
#发送邮件模块
import smtplib
#构造邮件模块
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#邮件发送人，第三方客户端登录授权码和接收人
from common.email_users import send_eamil,password,receiver_mail


def send_email():

    #邮箱服务器配置信息
    smtp_server ='smtp.qq.com'  #qq邮箱服务器
    port=465

    #邮件对象
    msg = MIMEMultipart('mixed')

    #邮件主题
    subject = time.strftime('%y-%m-%d %H:%M:%S') + "测试报告汇总"
    msg['Subject'] = subject
    msg['From'] = send_eamil
    msg['To'] = receiver_mail

    #添加邮件正文
    text_content=MIMEText('邮件正文')
    msg.attach(text_content)

    #添加邮件附件
    zipfile='E:\\GitHub\\Web_Framework\\email_files\\report.zip'
    file=open(zipfile,'rb')
    part = MIMEBase("application", "octet-stream")
    part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition', 'attachment', filename='report.zip')
    msg.attach(part)

    #发送邮件
    try:
        server=smtplib.SMTP_SSL(smtp_server,port)   #链接服务器
        server.login(send_eamil,password)   #登录邮箱
        server.sendmail(send_eamil,receiver_mail,msg.as_string())   #发送邮件
        print('send email success')
    except Exception:
        print('send email fail !!!')
    finally:
        server.quit()
