from python.Animal import Dog
from python.Student import Student
from python.Student3 import Student3

print(type(123))
print(type(True))
print(type(12.30))
print(type('String'))
print(type(None))
print(type(abs))
print(Dog());

s = Student("zhangsan",10);
print(s.telname)
print(Student.telname)
s.telname="zhangsan"
print(s.telname)
print(Student.telname)

##禁止Student添加私有属性
stu3=Student3()
stu3.age=100;
stu3.name="张三丰"
print(stu3.age)
print(stu3.name)
##禁止stu3添加额外的属性
#print(stu3.address)
print(s.__str__())
print(s.__repr__())

print(s())
