# 题目要求
# 使用Python中的csv模块, 在csv文件中写九宫格
# 题目讲解
# 回顾总结本节课csv的使用方法, 然后通过Python在test.csv文件中写入如下九宫格, 补全practice_csv.py中的代码:
# 书写代码

import csv
#from kkb_tools import open_file
with open("mytest.csv",'a')  as r:
    writer=csv.writer(r)
    writer.writerow([41,42,43])
    writer.writerow([51,52,53])
    writer.writerow([61,62,63])
print("写入完毕！")
#open_file("mytest.csv")