##绩效 统计

import pandas as pd
import os
import time
# 导入绘图模块
import matplotlib.pyplot as plt
# 指定文件夹的路径
firstPath = '/data/course_data/jixiao'
# 获取到 excel 文件夹下所有文件的名字
result = os.listdir(firstPath)
# 使用循环拼接路径
datelist = []
namelist = []
sectionlist = []
postlist = []
leaderlist = []
ratelist = []
leader_ratelist = []
for secondPath in result:
    # 拼接路径
    filePath=os.path.join(firstPath,secondPath)
    # 读取数据文件
    df = pd.read_excel(filePath,header=None)
    # 获取数据
    datelist.append(df.iloc[2,0])
    namelist.append(df.iloc[2,1])
    sectionlist.append(df.iloc[2,2])
    postlist.append(df.iloc[2,4])
    leaderlist.append(df.iloc[2,5])
    ratelist.append(df.iloc[2,6])
    leader_ratelist.append(df.iloc[9,7])
# 将获取到的数据创建成字典
data_dict = {
    '日期':datelist,
    '姓名':namelist,
    '部门':sectionlist,
    '岗位':postlist,
    '直属Leader':leaderlist,
    '评分':ratelist,
    '领导评分':leader_ratelist,
}
# 将字典数据转换成 DataFrame
data = pd.DataFrame(data_dict)
df = data.to_excel('绩效.xlsx')
df1 = pd.read_excel('绩效.xlsx')
# 将数据根据“领导评分”列进行排序
data = data.sort_values(by='领导评分',ascending=False)
result = data.groupby(by='评分').count()
group_count = result['日期']
# # 获取数据的索引，并转化成列表
index = group_count.index.tolist()
# # 获取数据的值，并转化成列表
values = group_count.values.tolist()
# # 绘制饼图
plt.figure(figsize=(10,10))
plt.pie(values,labels=index,autopct="%1.1f%%",startangle=150)
plt.savefig('绩效.png')
# # 展示图片
#plt.show()
#open_file("绩效.png")
time.sleep(0.5)
#open_file("绩效.xlsx")
print(df1)