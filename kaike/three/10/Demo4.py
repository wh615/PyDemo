##%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
x = [1,10,14,15,16,17]
y = np.array([3,4,6,2,1,5])

plt.figure(figsize = (10,8))
# 第一个子图
# 折线图
plt.subplot(2, 2, 1)
plt.plot(y)
plt.title('Axes1')
#第二个子图
# 折线图，y轴每个数据的立方
plt.subplot(2, 2, 2)
plt.plot(y**3)
plt.title('Axes2')
#第三个子图
# 折线图，x轴和y轴均指定数据
plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title('Axes3')
plt.show()