# 题目要求
# 复习今天所学的内容，编码、解码与文件读写，完成下面题目。
# 题目讲解
# 在practice_1601.py文件中补全代码，将注释中的bytes内容放入到代码中进行解码，将解码后的内容，写入到document_1601.txt文件中。 document_1601.txt的地址也写在注释中。


#书写你的代码
myfile = open(r'd:\\document_1601.txt','a')#a追加文件
myfile.write(b'\xe7\x9f\xa5\xe8\xa1\x8c\xe5\x90\x88\xe4\xb8\x80'.decode('UTF-8'))
myfile.close();