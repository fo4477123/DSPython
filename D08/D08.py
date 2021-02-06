import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']

sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']

weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]

rank_list = [8,1,5,4,7,6,2,3]

myopia_list = [True,True,False,False,True,True,False,False]

np.dtype({'names':('name','sex','weight','rank','myopia'),'format':(np.unicode,
np.unicode,np.float,np.int,np.bool)})