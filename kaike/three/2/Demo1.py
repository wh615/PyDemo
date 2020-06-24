from pandas import DataFrame, Series

emp=['001','002','003','004','005','006']
name=['亚瑟', '后裔','小乔','哪吒' ,'虞姬','王昭君']
series = Series(data=name,index=emp)
# 获取数据的值
print(series.values)
# 获取索引的值
print(series.index.tolist())
# 获取每对索引和值
print(list(series.items()))

print('####################################')
emp=['001','002','003','004','005','006']
name=['亚瑟', '后裔','小乔','哪吒' ,'虞姬','王昭君']
series = Series(data=name,index=emp)

# 使用索引值获取单个数据
print(series['001'])

# 使用索引值获取多个不连续的数据
print('索引下标',series[['002','004']])

print('#########################')
emp=['001','002','003','004','005','006']
name=['亚瑟', '后裔','小乔','哪吒' ,'虞姬','王昭君']
series = Series(data=name,index=emp)
# 获取单个数据
print(series[0])
# 获取多个不连续的数据
print('位置下标',series[[1,3]])
# 使用切片获取连续的数据
print('位置切片',series[0:3])
# 使用切片获取连续的数据
print('索引切片',series['001':'004'])

print('#####################')
for info in series:
    print(info)

print('#####################')
for info in series.values:
    print(info)
print('#####################')
for value in series.keys():
    print(value)

print('#####################')
for value in series.items():
    print(value)


print('##############')
import pandas as pd

df_dict = {
	'name':['ZhangSan','LiSi','WangWu','ZhaoLiu'],
	'age':['18','20','19','22'],
	'weight':['50','55','60','80']
}
df = pd.DataFrame(data=df_dict,index=['001','002','003','004'])
print(df)
# 获取行数和列数
print(df.shape)
# 获取行索引
print(df.index.tolist())
# 获取列索引
print(df.columns.tolist())

print('###########################################')
# 通过位置索引切片获取一行
print(df[0:1])
# 通过位置索引切片获取多行
print(df[1:3])
# 获取多行里面的某几列
print(df[1:3][['name','age']])
# 获取DataFrame的列
print(df['name'])
# 如果获取多个列
print(df[['name','age']])

# 获取数据的维度
print(df.ndim)