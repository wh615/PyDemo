import pandas as pd
import numpy as np
time_index = pd.date_range('2019-01-01', periods=400)
time_data = np.random.randint(100,size=400)
date_time = pd.Series(data=time_data,index=time_index)
print(date_time)


pd.to_datetime('2019年10月10日',format='%Y年%m月%d日')
