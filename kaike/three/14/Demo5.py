import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('../../data/iris.csv')
sns.pairplot(data)
plt.show()