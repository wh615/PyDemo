age=18
if age>=18:
    print("your age is",age)
    print("adult")

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

names = ['Michael', 'Bob', 'Tracy']

for name in  names:
    print(name)
    if(name.__eq__('Bob')):
        print("相等")

#使用range循环集合
for name in range(len(names)):
    print(names[name])

sum=0;

#rang不包含参数值 1-101之间数据求和不包含101
for i in range(101):
    sum+=i

print(sum)



names= ['Bart', 'Lisa', 'Adam']

print("=================")
for L in names:
    print("Hello",L)
