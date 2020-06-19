#由于BeautifulSoup不是Python标准库，在使用之前我们需要进行单独的安装。
# 如果你是在自己Windows环境下运行，需要在命令提示符内运行代码：pip install bs4。
# （MacOS环境下需要输入pip3 install BeautifulSoup4）我们的在线学习环境已经安装好了，可以直接使用

#安装失败可以使用  pip install bs4 -i https://pypi.douban.com/simple
# pip install openpyxl -i https://pypi.douban.com/simple

import requests
from bs4 import BeautifulSoup
#引入BS库
res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象
print(soup)
print(type(soup))