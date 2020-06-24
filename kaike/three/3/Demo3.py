import  pandas as pd
import random;

movice=pd.read_csv('./People_Information.csv')

print(type(movice))
print(movice.head())
director_name=movice['姓名'].tolist()
num =set(director_name);
print(len(num))