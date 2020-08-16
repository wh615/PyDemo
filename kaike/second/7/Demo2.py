# 题⽬要求：
#  根据已给⽹址爬取果壳前10⻚标题和对应的⽹址信息，并将爬取到的数据写⼊到excel表
# 格或则是CSV中。
# 使⽤技术点引导
#  requests
#  BeautifulSoup
#  for循环
#  openpyxl
# 地址：https://www.guokr.com/ask/highlight/?page=1
import requests
from bs4 import BeautifulSoup

import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='movie'
sheet['A1'] ='标题'
sheet['B1'] ='URL'
list_all = []
url='https://www.guokr.com/ask/highlight/?page={}'
for page in range(1,11):
    #print(url.format(page))
    res = requests.get(url.format(page))
    html = BeautifulSoup(res.text, 'html')
    datas=html.find_all('ul',class_='ask-list-cp')
    a=datas[0].find_all('div',class_='ask-list-detials')
    for i in a:
        res_data=i.find('a')
        #print("标题:",res_data.text)
        res_url=res_data['href']
        #print(res_url)
        # 电影评分信息，使用replace方法去掉多余的空格及换行符
        list_all.append([res_data.text, res_url])
        # 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all
        sheet.append([res_data.text, res_url])
#print(list_all)
wb.save('d:\\muoke.xlsx')
wb.close()

