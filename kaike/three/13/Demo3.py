
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def sinplot():
	x = np.linspace(0, 15, 100)
	for i in range(1, 3):
		plt.plot(x, np.sin(x + i))
# 设置图像风格
# sns.set(style='white')
# sns.set(style='whitegrid')
sns.set(style='darkgrid')
# sns.set(style='dark')
# sns.set(style='ticks')
sinplot()
sns.despine()
plt.show()