from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ['流浪地球','疯狂的外星人','飞驰人生','大黄蜂','熊出没·原始时代','新喜剧之王']
b = [38.13,19.85,14.89,11.36,6.47,5.93]

my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF')
plt.figure(figsize=(20,8),dpi=80)

# 绘制柱状图
rects = plt.bar(a,b,width=0.3,color=['red','green','blue','cyan','yellow','gray'])
plt.xticks(a,fontproperties=my_font)
plt.yticks(range(0,41,5),range(0,41,5))

# 在条形图上加标注(水平居中)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.3, str(height),ha="center")
plt.show()