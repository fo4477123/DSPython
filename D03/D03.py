
import numpy as np

v1=200
v0=20

v = np.divide(v1,v0)
l = np.log10(v)


Gdb = (20*l)

def CaculateGdb(vp):
    c = np.divide(vp,v0)
    lp = 20*np.log10(c)    
    return lp



print(CaculateGdb(20000))

V1_30 = 10**(30/20)*v0
V1_50 = 10**(50/20)*v0
V1_30/V1_50
print(V1_30/V1_50)

