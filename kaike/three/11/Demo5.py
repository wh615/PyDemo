# 《FIFA 19》是一款由EA加拿大、EA罗马尼亚开发由艺电发行的足球电子游戏。现在我们有一份包括最新版FIFA 2019球员属性的数据，数据路径为/data/course_data/data_analysis/FIFA19.xlsx,本数据共有10000条数据，数据的基本信息如下图：
# 题目讲解
# 现在根据上面的数据完成如下需求： 1. 统计出这些球员年龄的分布状态； 2. 统计出这些球员在球场位置的占比。 思路：获取球员年龄列数据，用直方图绘制球员年龄的分布状态；计算每个位置上球员的个数，用饼图绘制球场位置的占比；




#统计出这些球员年龄的分布状态参考答案：
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=10)
df = pd.read_excel('../../data/FIFA19.xlsx')

age_list = df['Age'].values.tolist()
# 设置组距
distance = 2
# 计算组数
group_num = int((max(age_list) - min(age_list)) / distance)
# 用直方图绘制分布状态
plt.hist(age_list, bins=group_num)
plt.xticks(range(min(age_list), max(age_list))[::2])
# 添加网格显示
plt.grid(linestyle="--", alpha=0.5)
# 添加x, y轴描述信息
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("球员数",fontproperties=my_font)
plt.show()


#统计出这些球员在球场位置的占比参考答案：
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('../../data/FIFA19.xlsx')
plt.figure(figsize = (10,8))
# 根据Position数据分组
num = df.groupby('Position').size()
plt.pie(num,labels = num.index, autopct='%.1f%%',shadow=False,startangle=90)

plt.show()