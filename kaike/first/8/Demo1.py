# 题目要求
# 通过自己方法，完成向上取整. 用户输入1.1，变成2 用户输入1.5，变成2 用户输入1.9，变成2
# 题目讲解
# 在这节课的案例中，我们使用了math.ceil()函数进行小数向上取整，我们能不能不使用math.ceil()函数，自己制作一个向上取整的函数。

def rounding(num):
    if num%1==0:
        return int(num)
    else:
    	data = int(num)+1
    	return data
while (True):
    num = float(input('请输入数字：'))
    num1 = rounding(num)
    print(num1)