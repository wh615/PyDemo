# 题目要求
# 学习使用time时间模块，计算某个函数执行所用的时间 。
# 题目讲解
# 计算函数def test()运行时所需要的时间， 首先在函数执行前打印记录下时间， 函数执行结束后打印记录下时间， 结束时间-开始时间就是函数运行所需的时间。
# 书写代码
import time
def test():
    startTime= time.time()
    time.sleep(3)
    endTime=time.time()
    consumingTime=endTime-startTime;
    print('方法执行耗时：{}'.format(int(consumingTime)))

test();