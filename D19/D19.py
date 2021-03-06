import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sk
import numpy as np

x = np.arange(20)
plt.title = "Bar fig"
plt.bar(x,np.random.rand(20),facecolor='red', edgecolor='white')
plt.xticks([]), plt.yticks([])
plt.show()

