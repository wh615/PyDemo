import  json,requests

session=requests.session
cookie_txt = open('cookie.txt', 'r')
#以reader读取模式，打开名为cookie.txt的文件。
cookie_dict = json.loads(cookie_txt.read())
#调用json模块的loads函数，把字符串转成字典。
cookie = requests.utils.cookiejar_from_dict(cookie_dict)
#把转成字典的cookie再转成cookie本来的格式。
session.cookies = cookie
#获取cookie：就是调用requests对象（session）的cookie属性。