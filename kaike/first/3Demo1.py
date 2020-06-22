height = 0;
while height < 170:
    height = int(input('继续输入身高：'))
print('已经找到人去搬水了~')

print('''课外题一:for 循环能确定循环次数while 不能确定循环次数 需要有跳出while循环的条件 break等''')

print('课外题二')
sum1 = 0;
for i in range(1, 101):
    sum1 += i;
print('使用for循环打印1-100之间的和：', sum1)

sum2 = 0;
i = 1;
while i < 101:
    sum2 += i;
    i+=1;
print('使用while循环打印1-100之间的和：', sum2)

print('课外题三 使用for 和while打印100以内的偶数')
for i in range(1, 101):
    if i % 2 == 0:
        print('使用for循环打印1-100之间偶数：', i)
i = 1;
while i < 101:
    if i % 2 == 0:
        print('使用while循环打印1-100之间的偶数：', i)
    i += 1;