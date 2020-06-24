#%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random
# 创建字体对象
my_font = font_manager.FontProperties(fname='../../data/STSONG.TTF',size=18)
x = range(0,120)
y = [random.randint(10,30) for i in range(120)]
# 添加字体属性
plt.ylabel("次数",fontproperties=my_font)
plt.xlabel("时间",fontproperties=my_font)
# 设置标题
plt.title('每分钟跳动次数',fontproperties=my_font)
plt.plot(x,y)
plt.show()