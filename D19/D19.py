import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sk
import numpy as np

x = np.arange(100)
plt.title = "Bar fig"
plt.bar(x,np.random.rand(100))
plt.xticks([]), plt.yticks([])
plt.show()

