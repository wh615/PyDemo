# 题目要求
# 请运用所给变量，使用str()函数打印两句话。
# 第一句话：1囚犯：你有什么能力来带我们出去?
# 第二句话：2 CA：我揍了希特勒200多次。
# 其中，变量会在【书写代码】提供，请直接【复制粘贴】：
# 题目讲解
# 在Python的江湖中，最常用的数据类型有三种：字符串(str)、整数(int)和浮点数(float)。
# 在数据拼接中，为了将不同的信息进行整合，可以使用拼接符号。但是，如果数据非字符串类型，则无法进行拼接。
# 此时，我们可以使用数据转换函数str()，将数据转换为字符串类型后，再进行拼接。
num1  = 1
num2  = 2
name1 = '囚犯'
name2 = 'CA'
word1 = '你有什么能力来带我们出去'
word2 = '我揍了希特勒200次'
fuhao1 = ':'

print(str(num1) + name1 + fuhao1 + word1)
print(str(num2) + name2 + fuhao1 + word2)


# 请运用所给变量，使用数据转换str()、int()、float()及数据拼接符号+,
# 打印一句话：美国队长2该片于2014年4月4日在北美与中国同步上映。
# 其中，变量会在【书写代码】提供，请直接【复制粘贴】：
# 题目讲解
#在数据拼接中，为了将不同的信息进行整合，可以使用拼接符号。但是，如果数据非字符串类型，则无法进行拼接。
# 此时，我们可以使用数据转换函数str()，将数据转换为字符串类型后，再进行拼接。并且针对不同类型的数据，
# 我们需要经历多次转换，最后才能转为字符串类型。（注意，题干给的数字是2.5哦，想想怎么把2.5转化成2））

name = '美国队长'
num = 2.5
word = '该片于2014年4月4日在北美与中国同步上映。'

print(name + str(int(num)) + word)

print("=======扩展题=====")
#一、题目：
#1. 分别写出三个变量：int类型一个，float类型一个，str类型一个，例如int类型：a = 1
#2. 查看定义三个变量的类型（type）并计算数值类型总值.
num1=100;
num2=12.90;
num3='100';
print(type(num1),type(num2),type(num3))
print('数值类型总和为：',float(num1)+float(num2)+float(num3))

#二、题目：
a="如果给这份爱加上一个期限我希望是"
b="9999.00"
c="1"
d="年"
#请根据我们提供的a,b,c,d变量 进行运算拼接处出： 如果给这份爱加上一个期限我希望是10000年.
print(a,int(eval(b)+eval(c)),d)

