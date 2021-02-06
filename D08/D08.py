import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']

sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']

weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]

rank_list = [8,1,5,4,7,6,2,3]

myopia_list = [True,True,False,False,True,True,False,False]

dt = np.dtype({'names':('Name', 'num1', 'num2', 'True'), 'formats':((np.str_, 5), np.int32, int, 'U3')})
newArray = np.dtype({'names':('Name','sex','weight','rank','myopia'),'formats':((np.str_, 5),(np.str_, 5),'f','i','?')})
a = np.zeros(8,dtype=newArray)

for i in range(len(name_list)):
    a[i]['Name'] = name_list[i]
    a[i]['sex'] = sex_list[i]
    a[i]['weight'] = weight_list[i]
    a[i]['rank'] = rank_list[i]
    a[i]['myopia'] = myopia_list[i]

print(np.average(a['weight']))

print('boy : 平均體重'+ str(np.average(a[a['sex']=='boy']['weight'])))

print('girl : 平均體重'+ str(np.average(a[a['sex']=='girl']['weight'])))
