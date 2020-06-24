# 题目要求
# 本练习我们继续使用Seaborn模块内置数据集，路径为：/data/course_data/data_analysis/tips.csv。
# 题目讲解
# 完成下面的要求： 1. 绘制出每两列变量之间的关系； 2. 不同性别的消费数据有没有明显的差别。 3. 绘制消费总额与小费两个变量的关系分布图。

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../../data/tips.csv')
# 绘制出每两列变量之间的关系
sns.pairplot(data)

# 不同性别的消费数据有没有明显的差别
sns.pairplot(data,hue='sex')
# 绘制消费总额与小费两个变量的关系分布图
sns.pairplot(data,vars=['total_bill', 'tip'],kind='reg', diag_kind='kde')
plt.show()