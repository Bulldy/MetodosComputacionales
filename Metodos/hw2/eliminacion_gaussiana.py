import numpy as np


N=3
R=np.random.rand(N,N+1)*10
R=np.array(((9.,1.,3.,7.),(4.,6.,2.,7.),(3.,7.,1.,1.)))

print(R)
for i in range(N-1):
    for j in range(i+1,N):
        factor=(R[j,i])/(R[i,i])
        for k in range(N+1):
            R[j,k]=R[j,k]-factor*R[i,k]
print(R)

for i in range(N):
    k=R[i,i]
    for j in range(N+1):
        R[i,j]=(R[i,j])/(k)

print (R)

I=[]

for i in range(N,0,-1):
    if(i==N):
        In=R[i-1,N]
        I.append(In)
    else:
        a=R[i-1,i:N]
        print(a)
        In=R[i-1,N]-np.dot(np.array(a),np.array(I))
        I.insert(0,In)
        print(I)
    
        
print (I)
