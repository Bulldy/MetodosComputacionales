import math
import numpy as np
import matplotlib.pyplot as plt
import random 


def f(m,x,theta):
    return (np.cos(m*theta-(x*np.sin(theta))))*(1/np.pi)


theta1=np.arange(0.0,3.146+3.146/1000,3.146/1000)
x=np.arange(0,20+0.001,0.01)
m=[0,1,2]
i0=[]
i1=[]
i2=[]

for i in x:
    l=1001
    h=np.pi/1000
    cont=0
    for k in range(l):
        if(k==0):
            cont=cont+f(0,i,k*h)/3
        elif(k==(l-1)):
            cont=cont+f(0,i,k*h)/3
        elif(k%2==0):
            cont=cont+f(0,i,k*h)*2
        elif(k%2==1):
            cont=cont+f(0,i,k*h)*4
    #El contador esta bien, no se porque no puedo meterlo a i0
    list.append(i0,cont)

for i in x:
    l=1001
    h=np.pi/1000
    cont=0
    for k in range(l):
        if(k==0):
            cont=cont+f(1,i,k*h)/3
        elif(k==(l-1)):
            cont=cont+f(1,i,k*h)/3
        elif(k%2==0):
            cont=cont+f(1,i,k*h)*2
        elif(k%2==1):
            cont=cont+f(1,i,k*h)*4
    list.append(i1,cont)

for i in x:
    l=1001
    h=np.pi/1000
    cont=0
    for k in range(l):
        if(k==0):
            cont=cont+f(2,i,k*h)/3
        elif(k==(l-1)):
            cont=cont+f(2,i,k*h)/3
        elif(k%2==0):
            cont=cont+f(2,i,k*h)*2
        elif(k%2==1):
            cont=cont+f(2,i,k*h)*4
    list.append(i2,cont)

fig1=plt.figure()
plt.plot(x,i0)
plt.plot(x,i1)
plt.plot(x,i2)


