#%matplotlib inline
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font =font_manager.FontProperties(fname='../../data/STSONG.TTF')
y1 = [1,0,1,1,2,4,3,4,4,5,6,5,4,3,3,1,1,1,1,1]
y2 = [1,0,3,1,2,2,3,4,3,2,1,2,1,1,1,1,1,1,1,1]

x = range(11,31)
# 设置图形
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y1,color='red',label='自己')

plt.plot(x,y2,color='blue',label='同事')

# 设置x轴刻度
xtick_labels = ['{}岁'.format(i) for i in x]

plt.xticks(x,xtick_labels,fontproperties=my_font,rotation=45)

plt.grid(alpha=0.4)

plt.legend(prop=my_font)

plt.show()