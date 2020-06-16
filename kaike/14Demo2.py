import csv

with open("d:\\test\\mytest.csv",encoding='utf-8-sig')  as r:
    print("内容如下\n")
    reader = csv.reader(r)
    #使用csv的reader()方法，创建一个reader对象
    for content in reader:
    #遍历reader对象的每一行
        print(content)

print("读取完毕！")

import csv
#from kkb_tools import open_file
with open("mytest1.csv",'a')  as r:
    writer = csv.writer(r)
    writer.writerow([41,42,43])
print("写入完毕！")
#open_file("mytest1.csv")

## 需要事先安排好pip install kkb模块
import csv
#from kkb_tools import open_file
with open("mytest.csv",'a')  as r:
    writer=csv.writer(r)
    writer.writerow([41,42,43])
    writer.writerow([51,52,53])
    writer.writerow([61,62,63])
print("写入完毕！")
#open_file("mytest.csv")

with open("mytest.csv",'r')  as r:
    reader=csv.reader(r)
    print(reader)
    for line in reader:
        print(line)
print('打印完毕')