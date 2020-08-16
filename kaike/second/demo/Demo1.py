import requests
from bs4 import BeautifulSoup
url='https: // platform.insnail.com / admin / api / consultuser / info / list?page = 1 & limit = 1000 & consultGroup = & nickName = h & userId = & sysUserId = & userGourps = & orderTime = & orderOrigin = 1 & serviceStatus = 4-5'
res = requests.get(url=url)
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='show-list-item')
print("想找的菜的信息都在这里了：")
for item in items:
    print(item) # 打印item

