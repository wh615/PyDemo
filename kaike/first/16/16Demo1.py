import csv #引入csv模块
#调用open()方法，文件名是detaillist.csv，追加模式"a", 文件名在代码中称为listfile
with open("detaillist.csv","a",newline='',encoding='GBK') as listfile:
    #使用csv.writer（）函数创建writer对象，用于写入
    writer = csv.writer(listfile, dialect='excel')
    #列表头部第一行的字段
    header = ['期次','偿还本息（元）','偿还本金（元）','偿还利息（元）']
    # 使用writer对象写入表头
    writer.writerow(header)