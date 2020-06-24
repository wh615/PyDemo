import pandas as pd
df1 = pd.read_csv('/data/course_data/data_analysis/2017_1_data.csv')
print(df1.shape)
df2 = pd.read_csv('/data/course_data/data_analysis/2017_2_data.csv')
print(df2.shape)
# 合并数据
df3 = pd.concat([df1,df2])
print(df3.shape)
print(df3.head())
# 倒序排列时间
df3.sort_values(by='Duration (ms)',ascending=False,inplace=True)
print(df3.head())
# 获取最长时间
long_time = df3.iloc[0]['Duration (ms)']
print(df3.head())
print(long_time)