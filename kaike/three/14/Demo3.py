import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
df = pd.DataFrame({'x': np.random.randn(500),
                   'y': np.random.randn(500)})
sns.jointplot(x='x', y='y', data=df, kind='hex')
plt.show()