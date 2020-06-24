
import pandas as pd
df = pd.read_excel('../../data/lagou.xlsx')
print(df.shape)
print(df.head())

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=10)
df = pd.read_excel('../../data/lagou.xlsx')
plt.figure(figsize = (10,8))
num = df.groupby('学历').size()
# 绘制饼图
patches, l_text, p_text = plt.pie(num,labels = num.index, autopct='%.1f%%',shadow=False,startangle=90)
for t in l_text:
    t.set_fontproperties(my_font)
plt.show()