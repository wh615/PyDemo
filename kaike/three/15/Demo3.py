import pandas as pd

# 2019年北京哪个月的气温波动最大
# （1）根据月份进行分组
# （2）计算每个组的温度极差（本月最高温度减去最低温度）
# （3）比较极差的大小
# 第一步： 处理数据
# 在读取日期的时候，利用parse_dates()方法将“日期”这列数据类型转换成datetime类型，这样方便我们可以根据时间获取数据
df = pd.read_csv('../../data/BJ_tianqi.csv',parse_dates=['日期'])
print(df.shape)
# 由于最高温度和最低温度两列数据类型都是带有"℃"符号的字符串，方便计算我需要去除“℃”，并将数据类型转化成int
df["最高温度"] = df["最高温度"].str.replace("℃", "").astype('int')
df["最低温度"] = df["最低温度"].str.replace("℃", "").astype('int')

# 方便分组计算，我们可以添加月份列
df['月份'] = df['日期'].dt.to_period("M")

# 根据月份分组，并计算每个组的极差值
dict1 = {
    "最高温度":'max',
    "最低温度":'min'
}
df_group = df.groupby(by='月份').agg(dict1)

# 计算每个月气温波动并，添加一列
df_group['极差'] = df_group['最高温度']-df_group['最低温度']
# # 根据极差进行排序
result = df_group.sort_values('极差')
print(result)
# 根据结果我们可以发现，2019年中3、4-5、5、10月份的气温波动都是比较大，温差比较大，请注意添减衣服，不要感冒呦。


# 2019年各种空气质量的占比是多少
# 空气质量的占比我们可以根据空气质量列进行分组
group_count = df.groupby(by='空气质量').count()
# 获取空气质量的种类
aqi_type = group_count.index.tolist()
# 获取每个种类的数量,可以获取分组后任何的一列数据即可
type_count = group_count['日期'].values.tolist()
# 根据数据绘制饼图
import matplotlib.pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=10)
patches, l_text, p_text=plt.pie(type_count,labels=aqi_type,autopct="%1.1f%%",)
for t in l_text:
    t.set_fontproperties(my_font)
plt.show()