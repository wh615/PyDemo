#1:假如 有一个修路工程，分组(每组五人) 分段进行 每组每天可以完成1公里的路程，人数不足一组的按一组分配，要求输入这段路的长度和人数输出完成这段工程的天数


import math
def calculate(km,nums):
    group=math.ceil(nums/5)
    day=math.ceil(km/group);
    print('完成这段工程的天数为:%d天'%day)
while True:
    km = math.ceil(float(input('请输入路段的长度：')))
    nums=float(input('请输人数：'))
    calculate(km,nums)
