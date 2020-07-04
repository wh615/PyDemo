list=[523, 435, 712, 566, 613, 675, 620, 689, 643]
list.sort();
list.reverse();
print(list);

list=[10000,8500,9000,7000,8000,8000,9000,20000,15000,16000,5000]
sum = 0
average = 0
for i in list:
    sum+=i;
average=sum/len(list)
print(average)

list=[]
##输入n个整数，从小到大排列数据
pickNum=int(input('请输入多少个数字：'))
for i in range(0,pickNum):
    num=int(input('请输入数字:'))
    list.append(num);
list.sort();
print(list)



