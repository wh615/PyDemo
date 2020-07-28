#document_1602.txt的地址，直接粘贴即可
#书写你的代码
info=input('请你输入内容')
myfile = open(r'd:\\document_1602.txt','a')#a追加文件
myfile.write("您输入的是："+info)
myfile.close();