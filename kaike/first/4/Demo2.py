
##方式一
for i in range(1, 101):
    if i % 7 == 0:
        print('这个数是7的倍数:{}'.format(int(i)))
##方式二
for i in range(1, 101):
    if i % 7 == 0:
        print('这个数是7的倍数:%d' % (i))

print('解释格式化输出：\\n为换行输出 %s为站位符操作')

print('''==========登录系统============
1.登录
2.注册
3.退出
''')
dic = {}
flag=True;
while flag:
    num = int(input('请输出操作编号:'))
    if num == 1:
        name = input('请输入姓名:')
        password = input('请输入密码:')
        if dic.get(name)!=None:
            print('登录系统成功')
        else:
            print('请重新输入序号登录操作')
            continue;
    elif num==2:
        name = input('请输入姓名:')
        password = input('请输入密码:')
        if dic.get(name) != None:
            print('用户已经注册，请检查')
        else:
            dic[name]=password
    elif num==3:
        flag = False;
        print('欢迎下次使用')
    else:
        flag=False;
        print('未匹配到用户的输入')


































































