# 把下厨房“本周最受欢迎菜谱”的“菜名、URL、食材”打印出来
#
# （PS:1.由于做题人太多，第三方网站将我们IP封了，导致不能爬取相关信息，请学员们在本地运行代码。有不明白的请咨询班主任及助教
#
# 2.本地编辑器工具及环境下载链接
#
# Mac版：https://pan.baidu.com/s/1lmGtpN6lZckYwcZqJgT7gA
#
# Win10版：https://pan.baidu.com/s/1q_r2aKPxyKiEsH4S3662gg
#
# 3.下载及使用说明：http://www.jiazhixiang.xyz/categories/『环境配置』-工欲善其事%EF%BC%8C必先利其器/）
#
# 2
# 把下厨房“本周最受欢迎菜谱”的“菜名、URL、食材”打印出来。
# 地址：http://www.xiachufang.com/explore/

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