import requests
from bs4 import BeautifulSoup
res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='show-list-item')
for item in items:
    title = item.find(class_='desc-title') # 在列表中的每个元素里，匹配属性class_='title'提取出数据
    material = item.find(class_='desc-material') #在列表中的每个元素里，匹配属性class_='desc-material'提取出数据
    step = item.find(class_='desc-step') #在列表中的每个元素里，匹配属性class_='desc-step'提取出数据
    print(title,material,step) # 打印提取出的数据
    print(type(title),type(material),type(step)) # 打印提取出的数据类型