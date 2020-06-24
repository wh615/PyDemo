# 题目要求
# 本次练习我们使用的是上海证券交易所A股股票日线数据，我们从中选取了某公司2016全年股票信息。共有106条数据，每条数据包含13列信息，文件的路径为/data/course_data/data_analysis/600001SH.xlsx，以下获取的前五条数据，根据数据绘制出2015全年的开盘价折线图。
# 题目讲解
# 需要思考的问题： 1. 标题设置中文 2. X轴数据重合 3. 在一个坐标系中画多个折线 这个些问题我们将在下节课中解决！大家提前思考一下

#%matplotlib inline
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('../../data/600001SH.xlsx')
x = df['日期'].values.tolist()
y = df['开盘价(元)'].values.tolist()
plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel("¥")
plt.title('open/Time')
plt.show()