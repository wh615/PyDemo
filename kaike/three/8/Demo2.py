# 第一步:明确目标
# 现在我们有一份某电商超市从2016年到2019年的部分销售数据，
# 路径为：/data/course_data/data_analysis/Commerce.xls
# 我们的字段有订单 ID，客户对象，订单日期，邮寄方式，地区，地区经理，销售额，数量，退回，
# 折扣等，在这些字段下面，一共有近一万条数据。
# 第二步:分析过程
# 请根据数据完成下面的需求： 1.
# 分别算出2016年到2019年，每年5月份的总销售额。
# 2. 2018年各地区的5月份的总销售额对比。

import pandas as pd
data = pd.read_excel('../../data/Commerce.xls')
# 了解数据基本情况
print(data.head())

# 将订单日期设置为数据的索引
data.index = data['订单日期']

# 分别计算每年5月份的销售额
sales16 = data['2016-05']['销售额'].sum()
sales17 = data['2017-05']['销售额'].sum()
sales18 = data['2018-05']['销售额'].sum()
sales19 = data['2019-05']['销售额'].sum()

# 获取2018年五月份数据
sales18 = data['2018-05']
# 根据地区分组
groups = sales18.groupby('地区')
# 分别计算各地区销售总额
for group_name,group_df in groups:
    sales_all = group_df['销售额'].sum()
    print('{}地区5月份总销售额是{}'.format(group_name,sales_all))