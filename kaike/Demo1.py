name = input('请输入姓名')
year = int(input('请输入工作年限，数字'))
money=0
def bonus(year):
    if year<1:
        money = 1000
    elif 1<=year<3:
     	money = 3000*year
    else:
        money=5000*year;
    return money

def res(name,year):
   	cash = bonus(year)
   	print('%s来了%d年,获得奖金%d元' %(name,year,cash))
res(name,year)



print(type('666'))  # <class'str'>
print(type(6666))  # <class'int'>
print(type([6666])) #<class'list'>

print(type(('6666')))
print(type({'name':"zhangsan"}))