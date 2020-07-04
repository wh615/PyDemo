# 题目要求
# 有一个列表list = ['hello','i','love','you'].请将列表中的love取出来并打印结果。
# 题目讲解
# 金刚狼暗恋凤凰女不知道如何开口，请你帮他找到love并打印出来

list = ['hello', 'i', 'love', 'you']
# 方法一
print(list[2])
# 方法二
for info in range(len(list)):
    if (list[info] == 'love'):
        print(list[info])


# 题目要求
# dic = {'女巫':29,'狼人':30,'平民':50,'猎人':40}, 你需要找到键为‘狼人‘的数据，然后删除，打印删除后的字典。
# 题目讲解
# 在童话镇里，狼人每天晚上都会起来，杀掉村里的一位平民。你需要将狼人查找出来，毒死他。

dic = {'女巫': 29, '狼人': 30, '平民': 50, '猎人': 40}
del dic['狼人']
print(dic)

# 请将列表中的金刚狼到叶问数据取出来，再将叶问删除，并添加一个你喜欢的电影名称
mv_list = ['西红柿首富', '银河护卫队', '金刚狼', '银河补习班', '叶问', '狮子王', '钢铁侠']

print('获取金刚狼数据：', mv_list[2])
del mv_list[4]
print('叶问删除后mv_list：', mv_list)
mv_list.append('黄飞鸿之西域雄狮')
print('添加喜欢电影后mv_list:', mv_list)

##================通讯录管理系统=============
# 1.增加姓名和手机
# 2.删除姓名
# 3.修改手机
# 4.查询所有用户
# 5.根据姓名查找手机号
# 6.退出程序
# 要求：运行的代码终端可以看到上面这个界面，使用字典存储你的好友手机号，选择对应的数字执行对应功能，例如选择增加姓名和手机号，等待用户输入后将手机号和姓名一并存储起来并显示存储成功,(使用字典存储，主要考察字典的存储功能)
dic = {}
print('''
================通讯录管理系统=============
1.增加姓名和手机
2.删除姓名
3.修改手机
4.查询所有用户
5.根据姓名查找手机号
6.退出程序''')
while True:
    num = int(input('请输入对应的序号做操作:'))
    if num == 1:
        name = input('请输入用户名:');
        telNum = input('请输入手机号:');
        dic[name] = telNum;
    elif num == 2:
        name = input('请输入删除的用户名称:');
        del dic[name];
    elif num == 3:
        name = input('请输入修改手机号的用户名:');
        telNum = input('请输入修改手机号:');
        dic[name] = telNum;
    elif num == 4:
        print(dic)
    elif num == 5:
        name = input('请输入用户名查询手机号:');
        print(dic[name]);
    elif num == 6:
        break;
    else:
        break;
