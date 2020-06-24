import pandas as pd
df = pd.read_csv('../../data/height_weight.csv')
print(df.shape)
print(df.head())


import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('../../data/height_weight.csv')
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)
# 使用scatter绘制散点图
plt.scatter(df['height'],df['weight'],alpha=0.5,c='red')
plt.show()