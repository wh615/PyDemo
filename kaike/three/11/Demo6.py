# 题目要求
# 俗话说：一入电商深似海，从此妹子是路人；要想让自己网店营业额增加，不仅要耐得住寂寞，还要勤总结善分析。下面是一份某电商的销售数据，数据的路径为：/data/course_data/data_analysis/E-Business.xlsx
# 题目讲解
# 现在根据上面的数据完成如下需求： 1. 统计不同地区的总销售额。 2. 统计各个地区的订单量的占比。 思路：根据地区将数据进行分组，用柱状图绘制各个地区的总销售额；用饼图绘制订单量的占比；


#不同地区的总销售额参考答案：
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=10)
df = pd.read_excel('../../data/E-Business.xlsx')
num = df.groupby('地区').size()
x = num.index.tolist()
y = num.values.tolist()
plt.figure(figsize=(20,8),dpi=80)
# 绘制柱状图
rects = plt.bar(x,y,width=0.3)
plt.xticks(x,fontproperties=my_font)
# 在条形图上加标注(水平居中)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.3, str(height),ha="center")
plt.show()

#各个地区的订单量的占比参考答案：
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=10)
df = pd.read_excel('../../data/E-Business.xlsx')
df.head()
num = df.groupby('地区').size()
# 绘制饼图
patches, l_text, p_text = plt.pie(num,labels = num.index, autopct='%.1f%%',shadow=False,startangle=90)
for t in l_text:
    t.set_fontproperties(my_font)
plt.show()