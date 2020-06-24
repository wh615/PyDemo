# 如何查看别人的薪水？
from pandas import Series,DataFrame

# 使用字典创建
index_list = ['001','002','003','004','005','006','007','008','009','010']
name_list = ['李白','王昭君','诸葛亮','狄仁杰','孙尚香','妲己','周瑜','张飞','王昭君','大乔']
age_list = [25,28,27,25,30,29,25,32,28,26]
salary_list = ['10k','12.5k','20k','14k','12k','17k','18k','21k','22k','21.5k']
marital_list = ['NO','NO','YES','YES','NO','NO','NO','YES','NO','YES']
dic={
    '姓名': Series(data=name_list,index=index_list),
    '年龄': Series(data=age_list,index=index_list),
    '薪资': Series(data=salary_list,index=index_list),
    '婚姻状况': Series(data=marital_list,index=index_list)
    }
df=DataFrame(dic)

# 方法一：遍历薪水列
for value in df['薪资']:
    print(value)

# 方法二：遍历薪水列
for index,row_data in df.iterrows():
    print(row_data['薪资'])

# 方法三：遍历薪水列
for col,col_data in df.iteritems():
    if col == '薪资':
        print(col_data)

# 获取最大薪资
for col,col_data in df.iteritems():
    if col == '薪资':
        # 将薪资中的k去掉并转化成float类型
        list1 = [float(value[:len(value)-1]) for value in col_data]
        # 排序
        max_salary = sorted(list1,reverse=True)[0]
        print(max_salary)
print('###################')
df
df.tail(2)
df.head(2)
df.values