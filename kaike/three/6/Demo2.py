import pandas as pd
df = pd.read_excel('../../data/forbes_2018.xlsx')
print()
groups = df.groupby('gender')
for group_name,group_df in groups:
    print(group_name,group_df.shape)
    f_mean = group_df['age'].mean()
    f_max = group_df['age'].max()
    f_min = group_df['age'].min()
    print('{}组的最大年龄是{}，最小年龄是{}，平均年龄是{}'.format(group_name,f_max,f_min,f_mean))