# 题目要求
# 数据可视化的时候，常常需要将多个子图放在同一个画板上进行比较，那我们就来练习一下，在同一个画板上画出你还记得的数学函数图形。
# 题目讲解
# 例如：x的平方、x的立方、以及平方根等。

import pandas as pd
from matplotlib import pyplot as plt
import math

x = range(0,10)
y1 = [i**2 for i in range(0,10)]
y2 = [i**3 for i in range(0,10)]
y3 = [i**0.5 for i in range(0,10)]

plt.figure(figsize = (10,8))
# 第一个子图
# 平方图
plt.subplot(2, 2, 1)
plt.plot(x,y1)
#第二个子图
# 立方图
plt.subplot(2, 2, 2)
plt.plot(x,y2)
#第三个子图
# 平方根图
plt.subplot(2, 2, 3)
plt.plot(x,y3)

plt.show()