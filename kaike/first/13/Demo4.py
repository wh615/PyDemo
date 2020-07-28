# 2:给定一段文字， 哈喽，小伙伴们大家好，今后我们要一起好好学习呀 请将这段话文字内容以utf-8格式编码写入文件
# 写入的内容是编码后的字符串 并且实现打开文件时在屏幕上打印文件的原内容

info='哈喽，小伙伴们大家好，今后我们要一起好好学习呀'
myfile = open(r'd:\\document_1602.txt','w',encoding='utf-8')#a追加文件
myfile.write(info)
myfile = open(r'd:\\document_1602.txt','w',encoding='utf-8')#a追加文件
print(myfile.read())
myfile.close();