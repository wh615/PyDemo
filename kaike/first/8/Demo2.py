# 题目要求
# 出租车车费计算方式如下：1、打车距离在3公里以内，只收起步价15元。2、距离在3公里~15公里，每1公里加3元。3、距离超过15公里后，每1公里加5元。请完成计价函数。
# 题目讲解
# 今天需要和BOSS朋友去吃饭，我们一起打车去市中心，我们想写一个程序，输入坐车公里数，就能自动计算车费。 出租车车费计算方式如下：

import math
def calculate(km):
    if km<=3:
        money = 15
    elif 3<km<=15:
        money = 15+(km-3)*3
    elif km>15:
        money = 15+12*3+(km-15)*5
    print('本次打车费用为:%d元'%money)
while True:
    km = math.ceil(float(input('请输入坐车的公里数:可以输入小数:')))
    calculate(km)
