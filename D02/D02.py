
import numpy as np

array1 = np.array(range(30))
print(array1.shape)
print (array1)

##1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")

array2=array1.reshape(5,6,order='F')
print(array2.shape)
print(array2)

#2.呈上題的array，找出被6除餘1的數的索引
index = np.where(array2%6==1)

print(index)
