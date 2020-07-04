#2：已知某运输公司规定运输价格 5KG一下20元，5KG以上每运输1KG货物另收2元(不足一公斤按一公斤计算) 设计一个函数 实现输入货物重量 计算出运送这批货物的需要的价格

import math
def calculate(kg):
    sum=0;
    if kg<=5:
       sum=20;
    else:
        kg=math.ceil((kg-5))
        sum=math.ceil(kg*2+20);
    print('运送这批货物的需要的价格为:%d元'%sum)
while True:
    kg = math.ceil(float(input('实现输入货物重量：')))
    calculate(kg)