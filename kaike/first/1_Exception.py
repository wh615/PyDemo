name=input('请输入相关值:');
try:
    print(name);
    #print(name1);
except NameError as errorMsg:
    print("错误信息:",errorMsg)

else:
    print("没有相关错误信息")


print(name1);