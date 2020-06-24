import pandas as pd
import numpy as np
#size参数是指定生成6行3列的数组
data = np.random.randint(0,100,size=(6,3))
names = ['张三','李四','王五']
exam = ['期中','期末']
index = pd.MultiIndex.from_product([names,exam])
df = pd.DataFrame(data,index=index,columns=['Java','Web','Python'])
print(df)

df.sort_index(level=0,ascending=False)
print(df)