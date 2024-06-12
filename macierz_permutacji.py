import numpy as np

n=4

N=np.zeros((n,n), dtype=int)
print("\n",N)

a=[0,1,2,3]
b=[1,3,0,2]
M=np.zeros((n,n), dtype=int)
M[a,b]=1
print("\n",M)


