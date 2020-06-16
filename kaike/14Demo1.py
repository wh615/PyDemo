import time;  # 引入time模块

ticks = time.time()  # 时间戳   每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())  # 本地时间  从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))  # 根据需求选取时间格式
print("本地时间为 :", localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 格式化成2016-03-20 11:45:39形式

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))  # 格式化成Sat Mar 28 22:24:24 2016形式

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))  # 将格式字符串转换为时间戳