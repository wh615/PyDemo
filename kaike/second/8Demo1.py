import requests
from bs4 import BeautifulSoup
#引入requests和bs

url='https://www.zhihu.com/people/lisanshui1230/posts?page=1'
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#使用headers
res=requests.get(url,headers=headers)
#用resquest模块发起请求，将响应的结果赋值给变量res。
print(res.status_code)
#检查状态码