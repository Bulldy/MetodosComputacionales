import numpy as np

data=np.loadtxt('data_C.txt')
Exi=[]
shape=data.shape
dims=shape[1]

for i in range(dims):
    x=data[:,1]
    ex=np.mean(x)
    Exi.append(ex)

sij=[]

for i in range(dims):
    for j in range(dims):
        s=np.mean(np.multiply(data[:,i]-Exi[i],data[:,j]-Exi[j]))
        sij.append(s)

cov=np.reshape(sij,(dims,dims))
print (cov)
