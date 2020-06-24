import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 创建dataframe: df
df = pd.DataFrame({'x': np.random.normal(size=500),
                   'y': np.random.normal(size=500)})
# 绘制双变量散点图
sns.jointplot(x='x', y='y', data=df,kind='reg')
plt.show()