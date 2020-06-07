class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        ##定义私有属性 不准外部修改数据
        self.__gender = gender

    def get_gender(self):
        return self.__gender;
    def set_gender(self,gender):
        self.__gender=gender;


if __name__ == '__main__':
    info=Student1("zhangsan","四年级")
    print(info.name)
    print(info.get_gender())
    info.set_gender("五年级")
    print(info.get_gender())
