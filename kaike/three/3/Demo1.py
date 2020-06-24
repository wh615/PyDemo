from pandas import Series,DataFrame
import pandas as pd

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

# 写入csv，path_or_buf为写入文本文件
df.to_csv(path_or_buf='./People_Information.csv', encoding='utf_8_sig')
print('end')

df = pd.read_csv('./People_Information.csv')
print(df)
print(df.shape)