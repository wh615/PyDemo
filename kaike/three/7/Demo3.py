# 题目要求
# 本次练习我们使用2017中国城市分级名单数据，共有300多条电影数据，每条数据包含7列信息，文件的路径为/data/course_data/data_analysis/china_city_list.xlsx，
#
# 数据详情
#
# City: 城市中文名称缩写
# City_FullName: 城市中文全称
# City_EN: 城市英文名称
# Province: 省中文名
# Province_EN：省英文名
# Region：区域划分（西、南、东、北
# Tier：城市等级（一线、二线、三线、四线、五线）
# 题目讲解
# 根据上面的数据，计算出我国南部所有城市中一线城市的占比是多少

import pandas as pd;
data=pd.read_excel('../../data/china_city_list.xlsx');

##根据区域和等级分组
groups=data.groupby(by=['Region','Tier'])

# 计算出所有区域内各个等级城市的数量
groups_count=groups.count();
# 计算出南部所有等级城市的总数量
south_all_count=groups_count.loc['South']['City'].sum()
south_t1_count=groups_count.loc['South','Tier 1']['City'].sum()

accounted=south_t1_count/south_all_count

print('南部所有城市中一线城市的占比是{}'.format("%.2f%%" % (accounted * 100)))