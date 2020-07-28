# 题目要求
    # 每个人都有多重身份， 比如说一个学生， 他在学校里的身份就是学生，进行学习；回到家里，
    # 他的身份就是儿子，需要照顾父母；他不仅有着学生的属性与方法，还有着儿子的属性与方法。
# 题目讲解
    # 创建一个学生类，拥有属性（stu_no学号），方法（study,会使用Python语言）
    # 创建一个孩子类，拥有属性（status身份），方法（care，照顾父母） 创建一个儿子类，继承于学生类与孩子类， 拥有两个类的属性与方法
class Student(object):
    stu_no='001'
    def study(self):
        print('使用Python编程');
class Child(object):
    status='孩子';
    def care(self):
        print('照顾父母');
class Son(Student,Child):
    pass;

xiaoming = Son()
print(xiaoming.stu_no)
print(xiaoming.status)
xiaoming.study()
xiaoming.care()