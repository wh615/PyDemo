import psutil
import requests

from python.MyHtmlParser import MyHTMLParser

r=requests.get('https://www.baidu.com/');
print(r.status_code)
print(r.text)
##print(MyHTMLParser(r.text))
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))