#1:创建一个类，要求在进行实例化的时候自动打印你的名称 并且调用类方法run 的时候打印出你的名称 星座 年龄

class MyInfo:
    def __init__(self,name,constellation,age):
        self.name=name
        self.constellation=constellation
        self.age=age
        print('姓名：',self.name);
    def run(self):
        print("姓名：%s,星座:%s,年龄：%d" %(self.name,self.constellation,self.age))
myInfo=MyInfo('zhangsan','狮子座',18);
myInfo.run();