import pandas as pd
books = pd.read_excel('/data/course_data/data_analysis/04Books.xlsx',index_col = 'ID')
print(books)

# 计算Price的值(这种方法是列与列之间对齐后进行计算)
books["Price"] = books['OnePrice'] * books['Count']
print(books)

# 如果只想算某一段就可以，使用循环迭代（是单元格与单元格之间的操作）
for i in range(5,16):
    books["Price"].iloc[i] = books["OnePrice"].iloc[i] * books["Count"].iloc[i]
print(books)