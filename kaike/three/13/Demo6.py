import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
data = pd.read_excel('../../data/births.xlsx')
# 根据年份进行分组
groups = data.groupby(by = ['year','gender'])
def subplot(gender):
    for group_name,group_df in groups:
        if gender in group_name:
            plt.bar(group_name[0],group_df['births'].sum())

with sns.axes_style("darkgrid"):
    plt.subplot(211)
    subplot('F')
with sns.axes_style("whitegrid"):
    plt.subplot(212)
    subplot('M')
plt.show()