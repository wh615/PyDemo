
L=[]
n=1
while n<=99:
    L.append(n);
    n=n+2;
print(L)
print(L[::10])

#切片处理
print(L[0:3])
print(L[:3])
print(L[1:3])

print(L[-2:])

print(list(range(100)))
#前10个数，每两个取一个
print(L[:10:2])
print(L[::10])

###列表式求值
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])


L = [x * x for x in range(10)]
print(L)

g=(x * x for x in range(10))
print(next(g))

