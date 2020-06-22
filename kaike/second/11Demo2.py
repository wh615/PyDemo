import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
#封装headers
url='http://www.weather.com.cn/weather/101020100.shtml'
#把URL链接赋值到变量url上
res=requests.get(url,headers=headers)
#发送requests请求，并把响应的内容赋值到变量res中
res.encoding='utf-8'
bsdata=BeautifulSoup(res.text,'html.parser')
#使用bs模块解析获取到的数据
data_temperature= bsdata.find(class_='tem')
#使用find()取出天气的温度数据
data_weather= bsdata.find(class_='wea')
#使用find()取出天气的文字描述
print(data_temperature.text)
#取出变量data_temperature中的字符串内容，并打印
print(data_weather.text)
#取出变量data_weather中的字符串内容，并打印