import numpy as np


#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a = np.arange(1,21)
print(a)



#a[start:end:step]
#2.呈上題，將以上數列取出偶數。
print(a[1::2])

#3.呈1題，將數列取出3的倍數。
print(a[2::3])

