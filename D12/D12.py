import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(200),index=pd.date_range('1/1/2020',periods=200))

ts=ts.cumsum()
print(ts)
ts.plot()
plt.show()

df = pd.read_csv('./D12/boston.csv')
print(df)
df.boxplot()

plt.show()

df.plot.scatter(x='NOX', y='DIS')

plt.show()

#指數下降的關係

