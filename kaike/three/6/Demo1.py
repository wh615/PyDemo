import pandas as pd
df = pd.read_excel('../../data/forbes_2018.xlsx')
group = df.groupby('gender')
for gender,value in group.size().items():
    # 计算每组的占比
    accounted = value/df.shape[0]
    # 将小数转化成百分数
    bb = "%.2f%%" % (accounted * 100)
    print('福布斯2018年度亿万富翁中{}共{}位，占比是{}'.format(gender,value, bb))