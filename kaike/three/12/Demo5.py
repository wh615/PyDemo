# 题目要求
# 本练习继续使用某电商超市从2016年到2019年的部分销售数据，路径为：/data/course_data/data_analysis/Commerce.xls。
# 题目讲解
# 请用一张图绘制出2018年各地区销售总额及增长率。

# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=18)

data = pd.read_excel('../../data/Commerce.xls')
# 将订单日期设置为数据的索引
data.index = data['订单日期']

# 2018年各季度各地区的总销售额
area_sales18 = data['2018'].groupby('地区')['销售额'].sum()

# 2017年各季度各地区的总销售额
area_sales17 = data['2017'].groupby('地区')['销售额'].sum()

# 增长率 = (area_sales18- area_sales17)/area_sales17
growth_rate = (area_sales18-area_sales17)/area_sales17

fig = plt.figure()
ax = fig.add_subplot(111)
lin1 = ax.bar(area_sales18.index,area_sales18.values)

ax.set_ylabel("2018销售额",fontproperties=my_font)
ax.set_xlabel("地区",fontproperties=my_font)
plt.xticks(growth_rate.index,fontproperties=my_font)

ax2 = ax.twinx()
lin2 = ax2.plot(growth_rate.index,growth_rate.values,color='red',marker='o')
ax2.set_ylabel("增长率",fontproperties=my_font)

# 绘制网格
ax.grid()
plt.show()