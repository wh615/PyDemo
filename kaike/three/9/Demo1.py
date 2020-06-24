#在使用jupyter notebook时调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候,需要加上%matplotlib
#%matplotlib inline


from matplotlib import pyplot as plt
x = range(1,9)
y = [17, 17, 18, 15, 11, 11, 13,99]
plt.plot(x,y)
plt.show()

#在使用jupyter notebook时调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候,需要加上%matplotlib
#%matplotlib inline

from matplotlib import pyplot as plt
x = range(1,8)
y = [17, 17, 18, 15, 11, 11, 13]
plt.plot(x, y, color='green',alpha=0.5,linestyle='-',linewidth=3,marker='o')
plt.show()


#在使用jupyter notebook时调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候,需要加上%matplotlib
#%matplotlib inline

from matplotlib import pyplot as plt
x = range(1,8)
y = [17, 17, 18, 15, 11, 11, 13]
plt.plot(x, y, color='green',alpha=0.5,linestyle='--',linewidth=6,marker='o')
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.xlabel('x轴')
plt.ylabel("y轴")
plt.title('标题')
plt.show()