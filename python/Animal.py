class Animal(object):
    def run(self):
        print("动物运动操作");

class Dog(Animal):

    def run(self):
        print("狗在跑")


class Cat(Animal):
    def run(self):
        print("猫在跑");

def run_twice(animal):
    animal.run();
    animal.run();




