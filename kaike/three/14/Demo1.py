
import numpy as np
import seaborn as sns
# 从标准正态分布中随机地抽取1000个数
data = np.random.normal(size=1000)
sns.set(style='darkgrid')
sns.distplot(data,kde=True)