import pandas as pd
df = pd.read_csv('/data/course_data/data_analysis/liupu.csv')
# 查看数据
print(df.head())

# series.str会将每一个数据转换成字符串
# contains()判断字符串是否含有指定子串，返回的是bool类型
bools = df['结尾'].str.contains("市")

# 根据人口数倒序排列
df = df[bools].sort_values('常住人口',ascending=False)
# 获取前十个数据
print(df.head(10))