


try:

    f=open("D:\\test\\wordcount.txt",'r')
    info=f.read();
    print(info);

    for name in range(10):
        f = open("D:\\test\\wordcount.txt", 'a');
        f.write("写入文件");
        f.write("\r\n");
finally:
    if f:
        f.close()



