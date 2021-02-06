import numpy as np
from numpy.core.defchararray import array
from numpy.core.fromnumeric import around

array1 = np.array([[10, 8], [3, 5]])
inv1 = np.linalg.inv(array1)

array3= np.dot(array1,inv1)
print(array3)

print(array3.shape)
result = True
count = 0
for arr in array3:
    for i in range(len(arr)):
        if(count == i and np.around(arr[i]) == 0):
            result = False
    count = count +1

if result == True:
    print("是單位矩陣")
else:
    print('不適單位矩陣')

w,v= np.linalg.eig(array1)

u,s,vh=np.linalg.svd(array1)