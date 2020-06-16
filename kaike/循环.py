for i in [1,2,3,4,5,6]:
    print(str(i)+'取钱')
print(i)

print(range(0,5))
print(range(11,20))

a=0
while a<4:
    a = a+1
print(a)


transformers= {'擎天柱':190,'大黄蜂':100,'救护车':100,'巨无霸福特':100,'红蜘蛛':100}

#遍历方式1
for key in transformers:
    print(key,transformers[key])
#遍历方式2
for value in transformers.values():
    print(value)

#遍历方式3

for key,value in transformers.items():
    print("key:",key,"value:",value)

