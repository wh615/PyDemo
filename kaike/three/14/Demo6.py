import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../../data/iris.csv')
# 双变量图像设置为回归图，单变量（对角线图）设置为核密度图
sns.pairplot(data, hue='species',vars=['sepal_length', 'sepal_width'],kind='reg', diag_kind='kde')
plt.show()