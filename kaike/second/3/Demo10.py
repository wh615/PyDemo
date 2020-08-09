# 2、题⽬要求
#  爬取西游记每回题⽬，将第⼀回到第⼀百⼀⼗九回的题⽬到爬取到本地。
# 使⽤技术点引导
#  使⽤BeautifulSoup4解析器
#  requests
# 地址为：https://www.shicimingju.com/book/xiyouji.html
import requests
from bs4 import BeautifulSoup

res=requests.get('https://www.shicimingju.com/book/xiyouji.html');
html=res.text;
soup=BeautifulSoup(html,"html.parser")
items=soup.find_all(class_='book-mulu')
contents=items[0].find_all('li')
#print(contents)
for data in range(100):
    print(contents[data].find('a').text)
