from python.Animal import Dog, Cat, Animal, run_twice
from python.Student import Student

info=Student("zhangsan",20)
msg=info.getMsg('白云区','广州')

print(info.name,info.age)
print(msg)

dog=Dog();
cat=Cat();
print(dog.run())
print(cat.run())

print(isinstance(cat,Cat))
print(isinstance(dog,Dog))
print(isinstance(dog,Animal))
print(run_twice(Animal()));
print(run_twice(Dog()));
print(run_twice(Cat()));




