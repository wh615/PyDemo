

class Grade(object):
    def __init__(self):
        self.grade='2020级';

class Clazz(object):
    def __init__(self):
        self.clazz='1班';
class Teacher(Grade,Clazz):
    def __init__(self,tname,course):
        Grade.__init__(self)
        Clazz.__init__(self)
        self.tname=tname
        self.course=course
    def run(self):
        print("年级: %s 班级:%s  姓名:%s,课程:%s"  %(self.grade,self.clazz,self.tname,self.course))

class Student(Grade,Clazz):
    def __init__(self,sname,age):
        Grade.__init__(self)
        Clazz.__init__(self)
        self.sname=sname
        self.age=age
    def run(self):
        print("年级: %s 班级:%s  姓名:%s 年龄：%d"  %(self.grade,self.clazz,self.sname,self.age))

teacher=Teacher("zhangsan","英语")
teacher.run()
stu=Student("lisi",20)
stu.run()