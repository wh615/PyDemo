#2：实现计算器的加减乘除的功能，并输出，利用函数实现
def add(num1,num2):
    return num1+num2;
def subtract(num1,num2):
    return num1-num2;
def multiply(num1,num2):
    return num1*num2;
def divide(num1,num2):
    return num1/num2;
print('''
=============菜单功能===============
1:加法运算
2：减法运算
3：乘法运算
4：除法运算
''')
while(True):
    fun1=int(input("请选择输入相关功能"))
    num1=int(input("请输入第一个数字"))
    num2=int(input("请输入第二个数字"))
    if fun1==1:
        print("数字 %d 数字 %d相加结果为:"%(num1,num2),add(num1, num2))
    elif fun1==2:
        print("数字 %d 数字 %d相加结果为:"%(num1,num2),subtract(num1, num2))
    elif fun1==3:
        print("数字 %d 数字 %d相加结果为:"%(num1,num2),multiply(num1, num2))
    elif fun1==4:
        print("数字 %d 数字 %d相加结果为:"%(num1,num2),divide(num1, num2))
    else:
        print("未找到对应的功能")