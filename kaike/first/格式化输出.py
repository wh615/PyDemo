#格式化输出


#  str 字符串 str() %s
#  int 字符串 int() %d
#  float 字符串 float() %f

name='zhangsan';
age=18;
height=180.60;

print(name,age,height)

print('姓名: %s年龄:%d身高:%f')
#方法一
print('姓名: %s 年龄:%d  身高:%f' %(name,age,height)) #float默认是保持六位小数
print('姓名: %s 年龄:%d  身高:%.1f' %(name,age,height)) #float默认是保持六位小数
print('姓名: %s 年龄:%d  身高:%.2f' %(name,age,height)) #float默认是保持六位小数

#方法二

print('姓名:{} 年龄:{} 身高:{}'.format(name,age,height)) #float默认是保持六位小数

print('我的姓名为：{}'.format(name))