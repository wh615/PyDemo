import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=18)

# 获取数据
datas = pd.read_excel('../../data/600001SH.xlsx')
datas.index = pd.to_datetime(datas['日期'])
feb_datas = datas['2015-02']

# 绘制图形
fig = plt.figure(figsize=(20,8),dpi=80)
ax = fig.add_subplot(111)
lin1 = ax.plot(feb_datas.index.strftime('%Y-%m-%d').tolist(),feb_datas['开盘价(元)'].values.tolist(),label='开盘价',color='red')
ax.set_ylabel("开盘价(元)",fontproperties=my_font)
ax.set_xlabel("日期",fontproperties=my_font)
ax.legend(prop=my_font)

ax2 = ax.twinx()
lin2 = ax2.plot(feb_datas.index.strftime('%Y-%m-%d').tolist(),feb_datas['成交量(股)'].values.tolist(),label='成交量(股)')
ax2.legend(prop=my_font)
ax2.set_ylabel("成交量(股)",fontproperties=my_font)

# 绘制网格
ax.grid()
plt.show()