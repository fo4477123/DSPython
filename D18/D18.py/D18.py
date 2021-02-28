import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,180)
y = np.cos(x)

# 開始畫圖
plt.plot(x,y)
# 在這個指令之前，都還在做畫圖的動作 
# 這個指令算是 "秀圖"
plt.show() 

plt.savefig("filename.png",dpi=300,format="png")

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
t = np.arange(0., 10., 0.7)
plt.scatter(X,Y,c='red')
plt.show()