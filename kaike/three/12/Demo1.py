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
lin1 = ax.plot(feb_datas.index.tolist(),feb_datas['开盘价(元)'].values.tolist(),label='开盘价',color='red')
ax.legend(prop=my_font,loc=0)
ax.set_ylabel("开盘价(元)",fontproperties=my_font)
ax.set_xlabel("日期",fontproperties=my_font)
plt.show()