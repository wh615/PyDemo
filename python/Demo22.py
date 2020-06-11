import os
import time
import pandas as pd


##合并表格操作
t1=time.time();
list=[];
n=0;
for file in os.walk('E:\\yonyou\\data'):
    for table in file[2]:
        path=file[0]+'/'+table;
        data=pd.read_csv(path,header=0,encoding='utf-8',engine='python')
        #data=pd.read_csv(path)
        n=n+1;
        list.append(data);
        print('第',str(n),'个表格已经提取')
data_result=pd.concat(list)
data_result.to_csv('E:\\yonyou\\data\\data_result.csv',index=0);
t2=time.time();
t=t2-t1
t=round(t,2);
print('用时',str(t),'秒')
print('完成')
