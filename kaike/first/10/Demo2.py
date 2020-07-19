class MaleGuests:
    def __init__(self,name,age,city):
        print('各位女嘉宾好')
        self.name=name;
        self.age=age;
        self.city=city;
    def sayHi(self):
        print('我叫%s,我今年%d岁,我来自%s' %(self.name,self.age,self.city))
        print('我叫{},我今年{}岁,我来自{}'.format(self.name,self.age,self.city))
shunquan = MaleGuests('孙权',28,'金陵')
shunquan.sayHi();
liubei = MaleGuests('刘备',28,'成都')
liubei.sayHi();