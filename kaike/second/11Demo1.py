import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
# 封装headers
url = 'http://www.weather.com.cn/weather/101020100.shtml'
# 把URL链接赋值到变量url上
res = requests.get(url, headers=headers)
res.encoding='UTF-8'
# 发送requests请求，并把响应的内容赋值到变量res中。
print(res.text)
# 打印出res对象的网页源代码
print(res.status_code)
# 检查响应状态是否正常
