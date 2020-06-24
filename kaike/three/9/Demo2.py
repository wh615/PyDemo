#%matplotlib inline
# 题目要求
# 本次练习我们使用上节课的爱奇艺视频数据，共有6万多条电影数据，每条数据包含12列信息，文件的路径为/data/course_data/data_analysis/aiqiyi.xlsx，以下获取的前五条数据，现在我们需要画出电影产量与年份的趋势图。
# 题目讲解
# 1. 根据年份将电影数据分组； 2. 分别计算每年的电影数量； 3. 根据电影年份和数量画出折线图。

import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('../../data/aiqiyi.xlsx')
# 根据上映时间分组
groups = df.groupby('上映时间')
# 根据评分获取出年份和数量的Series
num_series = groups['评分'].count()
# 获取出年份列表
year_list= num_series.index.tolist()
# 获取出数量列表
num_list= num_series.values.tolist()

# 绘制折线
plt.plot(year_list,num_list)
plt.xlabel('year')
plt.ylabel("Number")
plt.title('Number/year')
plt.show()