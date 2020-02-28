'''
发送邮件
'''

import smtplib
from email.mime.text import MIMEText


def send_email(subject):
    #邮箱服务器配置信息
    smtp_server ='smtp.qq.com'  #qq邮箱服务器
    port=465

    #邮件发送人和收件人信息
    send_eamil = '1976085712@qq.com'  # 发送方邮箱
    password = 'vnhakqrqvuopdgeh'  # 填入发送方邮箱的授权码
    receiver_mail = 'a1976085712@163.com'  # 收件人邮箱

    # 构建html格式邮件附件
    html_info=open(r'E:\GitHub\Web_Framework\report\cnode.html','rb').read()
    msg = MIMEText(html_info, 'html', 'utf-8')
    msg["Content-Disposition"] = 'attachment; filename="cnode.html"'

    #构建邮件主题和邮件头部发送人、收件人信息
    msg['Subject'] = subject
    msg['From'] = send_eamil
    msg['To'] = receiver_mail


    try:
        server=smtplib.SMTP_SSL(smtp_server,port)   #链接服务器
        server.login(send_eamil,password)   #登录邮箱
        server.sendmail(send_eamil,receiver_mail,msg.as_string())   #发送邮件
        print('send email success')
    except Exception:
        print('send email fail !!!')
    finally:
        server.quit()

