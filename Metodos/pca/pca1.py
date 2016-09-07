import numpy as np

data=np.loadtxt('data_C.txt')
Exi=[]

for i in range(3):
    x=data[:,i]
    ex=np.mean(x)
    Exi.append(ex)

sij=[]
for i in range(3):
    for j in range(3):
        s=np.mean(np.multiply(data[:,i]-Exi[i],data[:,j]-Exi[j]))
        sij.append(s)

cov=np.reshape(sij,(3,3))
print (cov)
