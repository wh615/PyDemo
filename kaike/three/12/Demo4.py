# 第一步:明确目标
# 绘制出一个段完整的正弦函数，如下图所示，不要显示坐标周以及刻度值。
# 第二步:分析过程
# 下面是需要用到的函数： numpy.linspace(start, stop, num=50)在指定的间隔内返回均匀间隔的数字，返回num均匀分布的样本，在[start, stop]。 numpy.sin(x)是numpy的提供的计算正弦值的函数。

import numpy as np
import matplotlib.pyplot as plt
# 在指定的间隔内返回均匀间隔的数字
x = np.linspace(-np.pi,np.pi,256)
# 正弦函数
y = np.sin(x)
#画图，使用不同的颜色和线条
plt.plot(x,y,color='blue',linewidth=1)
# 获得当前图表的图像
ax = plt.gca()

# 设置图型的包围线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
# 设置不显示坐标轴刻度
plt.xticks([])
plt.yticks([])

plt.show()