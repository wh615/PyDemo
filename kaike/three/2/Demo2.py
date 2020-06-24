import pandas as pd
df_dict = {
	'name':['ZhangSan','LiSi','WangWu','ZhaoLiu'],
	'age':['18','20','19','22'],
	'weight':['50','55','60','80']
}
df = pd.DataFrame(data=df_dict,index=['001','002','003','004'])
print(df)
# 获取某一行某一列的数据
print(df.loc['001','name'])
# 某一行多列的数据
print(df.loc['001',['name','weight']])
# 一行所有列
print(df.loc['001',:])
# 选择间隔的多行多列
print(df.loc[['001','003'],['name','weight']])
# 选择连续的多行和间隔的多列
print(df.loc['001':'003','name':'weight'])

print('########################################')
for index,row_data in df.iterrows():
    print(index,row_data)
print('########################################')
for col,col_data in df.iteritems():
    print(col)
    print(col_data)