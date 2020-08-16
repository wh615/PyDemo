# 1、题⽬要求
#  爬取猫眼电影信息，将电影名称，主演，上映时间爬取下来
# 使⽤技术点引导
#  requests
#  json
#  分析⽹址寻找⽬标⽹址
#  处理反爬技术-准备请求头
# 地址：https://maoyan.com/board
import requests
from bs4 import BeautifulSoup
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
res=requests.get('https://maoyan.com/board',headers=headers);
soup = BeautifulSoup(res.text, 'html.parser')
datas=soup.find_all('div',class_='movie-item-info')
for movie in datas:
    print("======")
    name = movie.find('p',class_='name')
    print(name.text.replace(' ',''))
    star = movie.find('p', class_='star')
    print(star.text.replace(' ',''))
    releasetime = movie.find('p', class_='releasetime')
    print(releasetime.text.replace(' ',''))
