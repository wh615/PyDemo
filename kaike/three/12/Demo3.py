import matplotlib.pyplot as plt
y = range(0,14,2)
x = [-3,-2,-1,0,1,2,3]

# 获得当前图表的图像
ax = plt.gca()

# 设置图型的包围线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('#0000FF')

plt.plot(x,y)
plt.show()