import pandas as pd;

data=pd.read_excel('../../data/china_city_list.xlsx')
groups = data.groupby(by=['Region','Tier'])

# 计算出所有区域内各个等级城市的数量
groups_count = groups.count()
# 获取分组后的索引
index_list = groups_count.index.tolist()

for value_tuple in index_list:
    # 区域内所有等级城市的总数量
    all_count = groups_count.loc[value_tuple[0]]['City'].sum()

    # 区域内各个城市等级的数量
    t_count = groups_count.loc[value_tuple[0], value_tuple[1]]['City']

    accounted = "%.2f%%" % (t_count / all_count * 100)

    print('{}所有城市中{}城市的占比是{}'.format(value_tuple[0], value_tuple[1], accounted))