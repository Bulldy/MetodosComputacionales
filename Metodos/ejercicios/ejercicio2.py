import numpy as np
import matplotlib.pyplot as plt
import random

g=-9.81
v0=1

def r(theta):
    R=(2*(v0**2)/g)*np.sin(theta)*np.cos(theta)
    return R

def cd1(theta,h):
    c=(r(theta+0.5*h)-r(theta-0.5*h))/h
    return c

def ed1(theta,h):
    e=(4*cd1(theta,0.5*h)-cd1(theta,h))/3
    return e

def cd2(theta,h1):
    c=(ed1(theta+0.5*h1,h1)-ed1(theta-0.5*h1,h1))/h1
    return c

def ed2(theta,h1):
    e=(4*cd2(theta,h1*0.5)-cd2(theta,h1))/3
    return e

tetha_i=[]
tetha_max=[]
tol=0.00001
h=0.00001
N=7

for i in range(N+1):
    ti=random.random()*0.5*np.pi
    tetha_i.append(ti)
    tii=ti
    while (abs(ed1(tii,h))>tol):
        tii=tii-(ed1(tii,h)/ed2(tii,h))
    else:
        tetha_max.append(tii)

print("Inicial.....Maximo")
for i in range(len(tetha_max)):
    print(round((tetha_i[i]*180/np.pi),1),round((tetha_max[i]*180/np.pi),10))
        
        
