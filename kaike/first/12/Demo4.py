# 在Bike基础上，创建子类Motorbike，子类Motorbike继承父类Bike。
#
# 在子类Motorbike中，改造父类init初始化方法；初始化方法中，增加默认参数motorbike=92，表示摩托车类使用的汽油号。
#
# 2第二步:分析过程
# 使用本节课案例中的Bike类，在Bike类基础上，创建子类Motorbike，改造初始方法，增加默认参数motorbike=92。
class Bike:
    # 初始化方法 no代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state
    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s' % (self.NO, self.age, status)
class Motorbike(Bike):
    # 初始化方法 no代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0, motorbike=92):
        self.NO = NO
        self.age = age
        self.state = state
        self.motorbike = motorbike
motorbike = Motorbike(1002, 1);
print(motorbike)
