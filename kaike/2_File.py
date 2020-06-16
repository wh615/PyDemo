
myfile = open('d:\\test\\friends.txt','r')
myfilecontent = myfile.read()
print(myfilecontent)
myfile.close()


myfile = open('d:\\test\\wordcount.txt','w')
myfile.write('从你的全世界路过、')
myfile.close();

myfile = open('d:\\test\\wordcount.txt','a')#a追加文件
myfile.write('从你的全世界路过、')
myfile.close();

#with自带关闭功能
with open('d:\\test\\wordcount.txt','a') as myfile:
    myfile.write('你好')