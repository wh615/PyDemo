import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

tag_name = bs_foods.find_all('p',class_='name')
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
list_all = []
for data in range(len(tag_name)):
    name=tag_name[data].text[18:-14].replace(' ','')
    url=tag_name[data].find('a')['href']
    content=tag_ingredients[data].text[1:-1].replace(' ','')
    print('菜名:%s\n地址:%s\n内容:%s\n' %(name,url,content))