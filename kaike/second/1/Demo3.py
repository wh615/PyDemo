# 1、题⽬要求：
#  请使⽤requests爬取⽂章，开掘⼀座⽂学理论富矿 并是⽤open⽅法将爬取的数据写⼊⽂
# 件data.txt中
# 地址为：https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc
# 注意：爬取下来的数据会是带标签的数据，不⽤担⼼后续我们会学习如果提取出存⽂本数据的
# ⽅法，⽬前我们主要练习requests这个库的使⽤
#pip install -i https://pypi.douban.com/simple  requests
import requests

res = requests.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc');
#res = requests.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc');
print(res.text)
content=res.content
file1=open('d:\\demo1.txt','wb')
file1.write(content)
file1.close()

