import pandas as pd
import numpy as np

data = np.random.randint(0,100,size=(8,4))
names = ['张三','李四','王五','Tom']
exam = ['期中','期末']
index = pd.MultiIndex.from_product([exam,names])
df = pd.DataFrame(data,index=index,columns=['Java','Web','Python','JavaScript'])
print(df)

import pandas as pd
s = pd.Series([1,2,3,4,5,6],index=[['张三','张三','李四','李四','王五','王五'],
                                   ['期中','期末','期中','期末','期中','期末']])
#print(s)
print(s['张三','期中'])