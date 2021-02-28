import pandas as pd
import numpy as np

index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)

print(series.to_period('W'))

print(series.resample('W').mean())