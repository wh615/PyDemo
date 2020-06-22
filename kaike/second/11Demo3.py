import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#引入schedule和time

def job():
    print("Working in progress...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'

#部署情况
schedule.every(1).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)
#检查部署的情况，如果任务准备就绪，就开始执行任务


import requests

from bs4 import BeautifulSoup



def get_weather():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101020100.shtml'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    bsdata = BeautifulSoup(res.text, 'html.parser')
    data_temperature = bsdata.find(class_='tem')
    data_weather = bsdata.find(class_='wea')
    return data_temperature,data_weather



#引入smtplib、MIMETex和Header

mailhost='smtp.qq.com';
qqmail = smtplib.SMTP()
qqmail.connect(mailhost,25)

sender = input('请输入你的邮箱：')
password = input('请输入你的密码：')
qqmail.login(sender,password)

receiver=input('请输入收件人的邮箱：')
content=input('请输入邮件正文：')
message = MIMEText(content, 'plain', 'utf-8')
subject = input('请输入你的邮件主题：')
message['Subject'] = Header(subject, 'utf-8')

try:
    qqmail.sendmail(sender, receiver, message.as_string())
    print ('邮件发送成功')
except:
    print ('邮件发送失败')
qqmail.quit()