import math


def my_abs(x):
    if(x>=0):
        return -x
    else:
        return -x

print(my_abs(100),my_abs(-100))


##返回多个值
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny = y + step * math.cos(angle)
    return nx,ny;

print(move(100,100,20,math.pi/6))

def power(x):
    return x * x


print(power(100))


def power(x,n=2):
    s=1;
    while n>0:
        n=n-1;
        s=s*x
        return s;

print(pow(5,3))


def enroll(name,gender,age=6,city='北京'):
    print(name,gender,age,city);

enroll('zhangsan','male')
enroll('zhangsan','male',100,'广州')

def calc(num):
    sum=0
    for i in num:
        sum+=i;
    return sum;

##print(calc(101))

print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2))

def method(x):
    if x==1:
        return 1
    else:
        return x+method(x-1);

print('计算方法',method(10))
print('计算方法',method(1000))