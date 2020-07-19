#2：创建一个类，初始化两个变量 name age定义两个类方法分别打印出姓名和年龄

class MyInfo:
    name='zhangsan'
    age=18
    def getNameInfo(self):
        print("姓名：%s" %(self.name))
    def getAgeInfo(self):
        print("年龄：",self.age);
myInfo=MyInfo();
myInfo.getNameInfo();
myInfo.getAgeInfo();