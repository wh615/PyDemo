
## 可以安装在线编辑工具 pip install jupyter -i https://pypi.douban.com/simple
## jupyter notebook --help 或jupyter notebook --h
## 启动 jupyter notebook
# 导入pandas模块
import pandas as pd
#通过Series存储每个英雄的基本信息
#创建Series
s1 = pd.Series([1001,'鲁班','18','150.00','男'])
s2 = pd.Series([1002,'小乔','19','167.00','女'])
s3 = pd.Series([1003,'关羽','30','180.00','男'])
s4 = pd.Series([1004,'蔡文姬','20','160.00','女'])
s5 = pd.Series([1005,'兰陵王','22','165.00','男'])
s6 = pd.Series([1006,'刘备','60','160.00','男'])

series_list=[s1,s2,s3,s4,s5,s6]
#创建一个DataFrame对象存储通讯录
df=pd.DataFrame(series_list)

# 打印刚刚构造的DataFrame
print(df)
print('############################################')
from pandas import Series,DataFrame

# 创建Series，使用默认索引
sel =  Series(data=[1,'TheShy',20,'天不生theshy，LPL上单万古如长夜'])
print(sel)
print('############################################')
# 导入Series
from pandas import Series,DataFrame

# 创建Series，使用自定义索引
sel =  Series(data=[1,'TheShy',20,'天不生theshy，Lpl上单万古如长夜'],
              index = ['排名','ID号','年龄','评语'])
print(sel)

print('############################################')
from pandas import Series,DataFrame
# 将字典转换为Series
dic={"red":100,"black":400,"green":300,"pink":900}
se2=Series(data=dic)
print(se2)

print('############################################')

lol_list=[['上单','TheShy',20],
            ['打野','小天',19],
            ['中单','Faker',23],
            ['ADC','Uzi',22],
            ['辅助','Ming',21]];
df=DataFrame(data=lol_list);
df1=DataFrame(data=lol_list,index=['a','b','c','d','e'],
               columns=['位置','ID号','年龄'])
print(df)
print(df1)
print('############################################')
# 使用字典创建
dic={
    '位置': ['上单', '打野', '中单', 'ADC','辅助'],
    'ID号': ['TheShy', '小天', 'Faker', 'Uzi', 'Ming'],
    'year': [20, 19, 23, 22,21]}
df=pd.DataFrame(dic)
print(df)