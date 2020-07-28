#1:定义一个父类初始化几个属性（属性自己定义） 定义一个子类继承父类的属性，并添加一些属性，
# 在子类定义一个方法 打印出子类的所有属性
class Father(object):
    name='lisi';
    age=30;
class Son(Father):
    name='liliu'
    age=8;
    address='西湖'
    def run(self):
        print("姓名：%s,年龄：%d,地址:%s" %(self.name,self.age,self.address))

son=Son();
son.run()
