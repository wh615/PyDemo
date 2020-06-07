' a test module '
from python.Student import Student

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    print("====",args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

bart = Student('BartSimpson', 59)
print(bart.name)
print(bart.age)

lisa = Student('Lisa Simpson', 87)
bart.age=8;
print(bart.age)
print(lisa.age)




