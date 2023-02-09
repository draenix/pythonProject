#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import sys
from email.mime.text import MIMEText
from email.header import Header
# from  mysql import *
from email.mime.multipart import MIMEMultipart

user = sys.argv[1]
ccuser = sys.argv[2]
sub = sys.argv[3]
content = sys.argv[4]
attaches = sys.argv[5:]

mail_host = "transport.mail.sohu-inc.com"
mail_postfix = "sohu-inc.com"


def send_mail(username, ccuser, sub, content, attaches):
    msg = MIMEMultipart()
    # c = MIMEText(content, 'plain', 'utf-8')
    c = MIMEText(content, 'html', 'utf-8')
    msg.attach(c)
    # msg = MIMEText(content,'html',_charset='utf8')
    msg['Subject'] = Header(sub, 'utf-8')
    # msg['From'] = 'tv-v-dc@sohu-inc.com'
    msg['To'] = username
    msg['cc'] = ccuser
    msg['Accept-Language'] = 'zh-CN'
    msg['Accept-Charset'] = 'ISO-8859-1,gbk'
    for att in attaches:
        print(att)
        attach = MIMEText(open(att, 'rb').read(), 'base64', 'gb2312')
        print(attach)
        attach["Content-Type"] = 'application/octet-stream'
        attach["Content-Disposition"] = 'attachment;filename="' + att + '"'
        msg.attach(attach)
    print("最终读取的是： " + msg.as_string())
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.sendmail('panther@sohu-inc.com', (username + ';' + ccuser).split(';'), msg.as_string())
        server.close()
        print("send mail success...")
    except Exception as e:
        print(e)
        return False

send_mail(user,ccuser,sub,content,attaches)