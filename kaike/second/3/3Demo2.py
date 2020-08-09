import requests
from bs4 import BeautifulSoup
res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='show-list-item')
print("想找的菜的信息都在这里了：")
for item in items:
    print(item) # 打印item