class Student(object):

    telname="学生名称";

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_score(self):
        print('%s: %s' % (self.name, self.age))

    def get_grade(self):
        if self.age >= 90:
            return 'A'
        elif self.age >= 60:
            return 'B'
        else:
            return 'C'
    def getMsg(self,address,city):
        self.address=address;
        self.city=city

        return address,city;

# bar=Student('lisi',20);
# print(bar.name)
# print(bar.age)
#
#
#
# bar.print_score()
# print(bar.get_grade())



