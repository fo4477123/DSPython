import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])
resultDF=_df.fillna('others')

print(_df)
print(resultDF)

pf = pd.get_dummies(resultDF[['Profession']])
resultDF = pd.concat([resultDF, pf], axis=1)
print(resultDF)


