# 2、题⽬要求：
#  请⾃动获取⽤户输⼊的关键字完成搜索 360的关键词接⼝是q 统计出输⼊关键字后爬取下
# 来数据的数量,通过捕获异常的⽅法如果爬取失败输出爬取失败字样

import requests
keyword = input(":")
try:
 kv = {'q':keyword}
 r = requests.get('http://so.com/s',params=kv)
 print(len(r.text))
except:
 print("爬取失败")