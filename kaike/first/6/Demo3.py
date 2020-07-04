
#编写一个程序：判断用户输入是否是一个数字
#如果是数字：则继续判断用户输入数字是否为7的倍数或者包含7，如果是，返回‘是’，否则返回结果‘否’
# 如果不是数字：则直接返回不是数字
num=input('请输入数据:')
flag=num.isdigit()
print(flag)
if flag:

    if int(num)%7==0:
        print('是')
    elif int(num)%10==7:
        print('是')
    else:
        print('否')
else:
    print('不是数字')
