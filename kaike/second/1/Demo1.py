# 题目要求
# 获取文章《蜀道难》全部内容，并且打印出全文内容。xa0xa0
# 题目讲解
# 文本URL:https://xiaoke.kaikeba.com/example/gexu/shudaonan.txt
# 1. 首先调用requests库，使用requests.get('URL')获取文件，返回的是Response对象。
# 2. 然后需要把Response对象用合适的数据形式返回。

#pip install -i https://pypi.douban.com/simple  requests

import requests

res = requests.get('https://xiaoke.kaikeba.com/example/gexu/shudaonan.txt');
novel = res.text
print(novel)
print(res.encoding,res.content,res.headers)
