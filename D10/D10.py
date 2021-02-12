import pandas as pd
import numpy as np

df1 = pd.read_csv('./D10/STOCK_DAY_0050_202009.csv')
df2 = pd.read_csv('./D10/STOCK_DAY_0050_202010.csv')

df3 = pd.concat([df1,df2])


print(df3)

df4 = df3[df3['open']<df3['close']]

print(df4)