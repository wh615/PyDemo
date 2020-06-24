# 题目要求
# 首先来了解一下数据，这是一份从2000年到2008年每个月新生婴儿数据，数据路径为：/data/course_data/data_analysis/births.xlsx。运行下方代码，查看数据具体信息：
# 题目讲解
# 使用matplotlib绘制出每年总出生数的柱状图，并使用seaborn设置一种风格。

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
data = pd.read_excel('../../data/births.xlsx')

# 根据年份进行分组
groups = data.groupby(by = 'year')
xticks = []
for group_name,group_df in groups:
    xticks.append(group_name)
    plt.bar(group_name,group_df['births'].sum())

# 设置x轴的显示范围
plt.xticks(xticks)
plt.xlabel('year')
plt.ylabel('births')
sns.set(style='darkgrid')
plt.show()