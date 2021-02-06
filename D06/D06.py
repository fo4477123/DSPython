from tokenize import String
import numpy as np
import gzip

zeroArray = np.zeros(20)

np.savetxt('./D06/test.out',zeroArray,delimiter=',')
loadArray = np.genfromtxt('./D06/test.out',delimiter=',')
print(loadArray)

array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open('./D06/D06.npz','wb') as f:
    np.savez(f,array1=array1,array2=array2)

npzfile = np.load('./D06/D06.npz')
m1 = np.load('./D06/SampleFile/multi_array.npz')

m2 = np.load('./D06/SampleFile/test.npy')
m3 = np.load('./D06/SampleFile/one_array.npy')

t1 = np.genfromtxt('./D06/SampleFile/names.txt',delimiter=',',names=True)
t2 = np.genfromtxt('./D06/SampleFile/test.csv',delimiter=',')
t3 = np.loadtxt('./D06/SampleFile/test.gz',delimiter=',')

t4 = np.genfromtxt('./D06/SampleFile/test.out',delimiter=',')
t5 = np.genfromtxt('./D06/SampleFile/transform.txt',delimiter=',',dtype=None)

print('test')

with open('./D06/D06_Final.npz','wb') as f:
    for file in m1.files:
        np.savez(f,'wb',m1[file])
    np.savez(f,'wb',m2)
    np.savez(f,'wb',m3)
    np.savez(f,'wb',t1)
    np.savez(f,'wb',t2)
    np.savez(f,'wb',t3)
    np.savez(f,'wb',t4)
    np.savez(f,'wb',t5)

