# 题目要求
# 循环打印1到10之间到数字，排除数字4
# 题目讲解
# 陈赫学习了for循环之后，他想循环打印1到10，但是他不喜欢数字4，不想让数字4打印出来。请你帮陈赫完成这个练习（提示：“不等于”用“!=”表示）
for i in range(1,11):
    if i!=4:
        print(i)




# #第一步:明确目标
# 需要循环输入跑男团队每个人的身高，只要找到一个身高高于170的就去搬水；如果找不到，就一直循环
#
# 第二步:分析过程
# 跑男团队今天接到一个任务，个子高的童鞋去搬水。

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

print('课外题三 使用for 和while打印100以内的偶数之和')
sum3=0;
for i in range(1, 101):
    if i % 2 == 0:
        sum3+=i
print('使用for循环打印1-100之间偶数：', sum3)
sum4=0;
i = 1;
while i < 101:
    if i % 2 == 0:
        sum4+=i
    i += 1;
print('使用while循环打印1-100之间的偶数偶数之和：', sum4)