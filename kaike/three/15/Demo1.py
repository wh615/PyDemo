import pandas as pd
data = pd.read_csv('../../data/analyse_spider.csv',encoding='GBK')
data.head()
# 删除businessZones列数据
data.drop(['businessZones'],axis=1, inplace=True)
data.dropna(inplace=True)

# 计算重复的数据数
print(len(data.duplicated()[data.duplicated()==True]))
# 删除重复数据
data.drop_duplicates(inplace=True)
data.info()


# 定义拆分的函数
def split_salary(salary, method):
    # 获取'-'索引值
    position = salary.upper().find('-')
    if position != -1:  # salary值是15k-25k形式
        low_salary = salary[:position - 1]
        high_salary = salary[position + 1:len(salary) - 1]

    else:  # salary值是15k以上形式
        low_salary = salary[:salary.upper().find('K')]
        high_salary = low_salary
    # 根据参数用以判断返回的值
    if method == 'low':
        return low_salary
    elif method == 'high':
        return high_salary
    elif method == 'avg':
        return (int(low_salary) + int(high_salary)) / 2


# 赋值
data['low_salary'] = data.salary.apply(split_salary, method='low')
data['high_salary'] = data.salary.apply(split_salary, method='high')
data['avg_salary'] = data.salary.apply(split_salary, method='avg')
print(data)