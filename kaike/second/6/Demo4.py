# 3、题⽬要求：
#  根据已给⽹址爬取果壳前10⻚标题和对应的⽹址信息
# 使⽤技术点引导
#  requests
#  BeautifulSoup
#  for循环
# 地址：https://www.guokr.com/ask/highlight/?page=1
import requests
from bs4 import BeautifulSoup

url='https://www.guokr.com/ask/highlight/?page={}'
for page in range(1,11):
    #print(url.format(page))
    res = requests.get(url.format(page))
    html = BeautifulSoup(res.text, 'html')
    datas=html.find_all('ul',class_='ask-list-cp')
    a=datas[0].find_all('div',class_='ask-list-detials')
    for i in a:
        res_data=i.find('a')
        print("标题:",res_data.text)
        res_url=res_data['href']
        print(res_url)
    print("====")



