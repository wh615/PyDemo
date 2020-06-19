import requests
import json
# 引入json模块
# 引用requests库
#而如果你想在Python语言中，实现列表/字典转json，
# json转列表/字典，则需要借助json模块。json模块不在我们的教学范围之内，所以不做展开。
# 你可阅读它的官方文档来了解，地址在这里：https://docs.python.org/3/library/json.html
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=65805191174562925&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
#requests.post
json1=res_music.json();
print(json1)
print(type(json1))

a = {"title": "今天是学习爬虫的第1天！", "date":"2019.10.1", "content":"今天是学习爬虫的第1天！我学习了爬虫基础啦！"}
b = json.dumps(a) #json转换成字典
c = json.loads(b)#字典转换成json
print(c)

print(type(c))