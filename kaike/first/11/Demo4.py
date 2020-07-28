#2：定义一个父类Computer，定义一个子类继承该父类，添加电脑品牌品牌属性，
#重写颜色和价格属性，并打印，实现无论输入什么颜色的全部打印红色 价格都是5000

class Computer(object):
    def __init__(self,color,price):
        self.color=color;
        self.price=price;
class ComnputerSon(Computer):
    color = '红色'
    price = 5000
    def __init__(self,brand):
        self.brand=brand
    def run(self,color,price):
        print("颜色：",self.color);
        print("价格：", self.price);
        print("品牌：", self.brand);
        print("统一输出样式：颜色:%s,价格:%d,品牌:%s" %(self.color,self.price,self.brand));

son=ComnputerSon('戴尔');
son.run('黑色',8000)