# 题目要求
# 本次练习采用的是爱奇艺视频数据。共有6万多条电影数据，每条数据包含12列信息，文件的路径为/data/course_data/data_analysis/aiqiyi.xlsx，以下获取的前五条数据：
# 题目讲解
# 1. 取出每年电影评分前两名电影的名字 2. 哪一年的电影总评分最高

#第一题答案
import pandas as pd
df = pd.read_excel('../../data/aiqiyi.xlsx',sheet_name='Sheet1')
groups = df.groupby('上映时间')
for group_name,group_df in groups:
    result = group_df.sort_values(by='评分',ascending=False)[0:2]
    print(group_name,result['整理后剧名'])
#第二题答案
import pandas as pd
df = pd.read_excel('../../data/aiqiyi.xlsx')
groups = df.groupby('上映时间')
year=groups.sum().sort_values(by='评分',ascending=False).index.to_list()[0]
print(year)