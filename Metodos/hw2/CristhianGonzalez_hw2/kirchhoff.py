import numpy as np
import sys

stringfile=str(sys.argv[1])

data=np.loadtxt(stringfile)
N=int(data[0])
R1=data[1]
R2=data[2]
V1=data[3]
V2=data[4]
R=np.zeros((N,N+1))
I=[]

#Si N==1 no hay matriz
if N==1:
    ii=(V1-V2)/(2*R1+R2)
    I.append(ii)

#Introducimos los valores a la matriz R                                         
for i in range(N):
    if (i%2==0):
        R[i,i]=2*R1+R2
        R[i,-1]=V1-V2
        if (i!=0):
            R[i,i-1]=-1*R1
            R[i-1,i]=-1*R1
    if (i%2==1):
        R[i,i]=2*R2+R1
        R[i,-1]=V2-V1
        R[i,i-1]=-1*R2
        R[i-1,i]=-1*R2

#Empieza reduccion gaussiana                                                    
for i in range(N-1):
    for j in range(i+1,N):
        factor=(R[j,i])/(R[i,i])
        for k in range(N+1):
            R[j,k]=R[j,k]-factor*R[i,k]

#Normalizar la diagonal                                                         
for i in range(N):
    k=R[i,i]
    for j in range(N+1):
        R[i,j]=(R[i,j])/(k)

#Solucion al sistema de ecuaciones                                              
for i in range(N,0,-1):
    if(i==N):
        In=R[i-1,N]
        I.append(In)
    else:
        a=R[i-1,i:N]
        In=R[i-1,N]-np.dot(np.array(a),np.array(I))
        I.insert(0,In)

file=open('corrientes.dat','w')
for i in range(len(I)):
    file.write("%f \n" %I[i])
file.close()
