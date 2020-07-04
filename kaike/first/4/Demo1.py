

print('''给定一个字符串 a=2123456请将a中除去2以外的数字输出，并且当数字为5时结束循环''')
a='2123456';
for i in a:
    if i!='2':
        print(i)
        if i=='5':
            break;


print('求一百以内，除去偶数，所有数之和')
sum=0;
for i in range(0,101):
    if i%2!=0:
        sum+=i;
print(sum)






