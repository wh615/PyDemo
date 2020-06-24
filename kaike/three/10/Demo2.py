#%matplotlib inline
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('../../data/600001SH.xlsx')
df.head()
x = df['日期'].values.tolist()
y = df['开盘价(元)'].values.tolist()

plt.figure(figsize=(20, 10),dpi=80)

plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel("¥")
plt.title('open/Time')
plt.show()