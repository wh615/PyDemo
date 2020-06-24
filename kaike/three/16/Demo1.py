from pandas import Series
import pandas as pd
emp=['001','002','003','004','005','006']
name=['亚瑟', '后裔','小乔','哪吒' ,'虞姬','王昭君']
series = Series(data=name,index=emp)
# 获取多个不连续的数据
print('位置下标',series[[1,3]])
# 使用切片获取连续的数据
print('位置切片',series[0:3])

df_dict = {
 'name':['ZhangSan','LiSi','WangWu','ZhaoLiu'],
 'age':['18','20','19','22'],
 'weight':['50','55','60','80']
}
df = pd.DataFrame(data=df_dict,index=['001','002','003','004'])
print(df)
# 通过位置索引切片获取一行
print(df[0:1])
# 通过位置索引切片获取多行
print(df[1:3])
# 获取多行里面的某几列
print(df[1:3][['name','age']])