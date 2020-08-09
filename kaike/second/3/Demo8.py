# 1、题⽬要求：
#  请使⽤requests爬取⽂章，开掘⼀座⽂学理论富矿。并要求使⽤BeautifulSoup4提取出⽂
# 本数据，将所有的标签部分去掉。
# 地址为： https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc
import requests
from bs4 import BeautifulSoup
res = requests.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc')
html=res.text;
soup=BeautifulSoup(html,'html.parser')
items=soup.find_all(class_='article-content')
title=items[0].find_all('p')
for data in range(8):
    res = title[data].find('span',class_="bjh-p")
    print(res.text)