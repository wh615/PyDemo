# 题目要求
# 本次练习采用的是网易考拉海淘网口红一天的销售数据。每条数据都包含了品牌、折扣价、原价、是否自营、评论数、国家共6列信息。文件的路径为data/course_data/data_analysis/lipsticks.xlsx
#
# 题目讲解
# 1. 统计每种口红的平均折扣价。 2. 分别统计每种口红自营评论数总和和非自营的评论数总和。
# 书写代码

import pandas as pd
df = pd.read_excel('../../data/lipsticks.xlsx')
print(df.head())

# 1. 统计每种口红的平均折扣价。
# 根据品牌进行分类
groups = df.groupby('品牌')
for group_name,group_df in groups:
    mean = group_df['折扣价'].mean()
    str_mean = '{}的平均折扣价为{}'.format(group_name,mean)
    print(str_mean)

# 2. 分别统计每种口红自营评论数总和和非自营的评论数总和
# 根据品牌列和是否自营列进行分组
groups = df.groupby(['品牌','是否自营'])
for group_name,group_df in groups:
    group_sum = group_df['评论数'].sum()
    str_sum = '{}{}的评论数为{}'.format(group_name[0],group_name[1],group_sum)
    print(str_sum)