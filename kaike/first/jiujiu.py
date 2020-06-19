for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}='.format(j,i),i*j,end=' ')
    print(' ')


for i in range(1,10):
    print( '%d X %d = %d' % (i,9,i*9) ,end = '  ' )
print('')



for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
    print('  ')



list=[523, 435, 712, 566, 613, 675, 620, 689, 643]
list.sort()
list.reverse()
print(list)


list=[10000,8500,9000,7000,8000,8000,9000,20000,15000,16000,5000]
sum = 0
average = 0
for i in list:
    sum+=i;

    print(sum)
average=sum/len(list)
print(average)