# 题目要求
# 本练习继续使用某电商超市从2016年到2019年的部分销售数据，
# 路径为：/data/course_data/data_analysis/Commerce.xls。
# 题目讲解
# 1. 计算出2018年各个季度的总销售额（1-3月为第一季度，
# 4-5-6为第二季度，7-9为第三季度，10-12为第四季度）。
# 2. 计算出2018年各季度各地区的总销售额。

import pandas as pd
data = pd.read_excel('../../data/Commerce.xls')

# 将订单日期设置为数据的索引
data.index = data['订单日期']

# 根据本节课知识点，分别获取每个季度销售总额
Q1 = data['2018-01':'2018-03']['销售额'].sum()
Q2 = data['2018-04':'2018-06']['销售额'].sum()
Q3 = data['2018-07':'2018-09']['销售额'].sum()
Q4 = data['2018-10':'2018-12']['销售额'].sum()
print('2018年Q1总销售额{},Q2总销售额{},Q3总销售额{},Q4总销售额{}'.format(Q1,Q2,Q3,Q4))

# 2018年各季度各地区的总销售额
# 获取每个季度的数据
Q1_area = data['2018-01':'2018-03'].groupby('地区')['销售额'].sum()
Q2_area = data['2018-04':'2018-06'].groupby('地区')['销售额'].sum()
Q3_area = data['2018-07':'2018-09'].groupby('地区')['销售额'].sum()
Q4_area = data['2018-10':'2018-12'].groupby('地区')['销售额'].sum()

print("""
2018年各季度各地区的总销售额:
Q1:{}
Q2:{}
Q3:{}
Q4:{}
""".format(Q1_area,Q2_area,Q3_area,Q4_area))


import  datetime

date=datetime.datetime.now()
date.str

