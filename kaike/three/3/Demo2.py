# 1. 球员信息存储在csv中，路径为/data/course_data/data_analysis/players.csv
# 2. 打印前5条了解数据的基本信息；
# 3. 随机获取5条数据。


import pandas as pd
import random
# 1. 读取数据
players = pd.read_csv('/data/course_data/data_analysis/players.csv')
# 2. 打印前5条了解数据的基本信息
print(players.head())
# 3. 随机获取5条信息
index_list = players.index.tolist()
for i in range(0,5):
    value = index_list[random.randint(0,len(index_list))]
    msg = players.iloc[value]
    print(msg)