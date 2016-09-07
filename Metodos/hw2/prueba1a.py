import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

#T=np.logspace(0.1,8)
v=np.logspace(10,14)

def I(v,T):
    v3=np.power(v,3)
    k=(2*sc.h/(sc.c**2))*(v3)
    div=1/(np.expm1(sc.h*v/(sc.k*T)))
    II=np.multiply(k,div)
    return II

def dI1(v,T):
    v2=np.power(v,3)
    v3=np.power(v,2)
    em1=1/(np.expm1(sc.h*v/(sc.k*T)))
    em2=np.power(em1,2)
    e=np.exp(sc.h*v/(sc.k*T))
    k1=(6*sc.h/(sc.c**2))*v2
    k2=(2*(sc.h**2)/((sc.c**2)*sc.k*T))*v3
    dI1=np.multiply(k1,em1)-np.multiply(np.multiply(k2,em2),e)
    return dI1

def dI2(v,T):
    v3=np.power(v,3)
    v2=np.power(v,2)
    em1=1/(np.expm1(sc.h*v/(sc.k*T)))
    em2=np.power(em1,2)
    em3=np.power(em1,3)
    e=np.exp(sc.h*v/(sc.k*T))
    e2=np.power(e,2)
    k1=(12*sc.h/(sc.c**2))*v
    k2=(12*(sc.h**2)/((sc.c**2)*sc.k*T))*v2
    k3=(4*(sc.h**3)/((sc.c**2)*(sc.k**2)*(T**2)))*v3
    k4=(2*(sc.h**3)/((sc.c**2)*(sc.k**2)*(T**2)))*v3
    dI2=np.multiply(k1,em1)-np.multiply(np.multiply(k2,em2),e)+np.multiply(np.multiply(k3,em3),e2)-np.multiply(np.multiply(k4,em2),e)
    return dI2

def cd1(v,T,h):
    didv=(I(v+0.5*h,T)-I(v-0.5*h,T))/h
    return didv

def ed1(v,T,h):
    didv=(4*cd1(v,T,0.5*h)-cd1(v,T,h))/(3)

#Debe tener la siguiente forma (funcion,v,T,h) 
#def CD(I,*E):
    #dIdv=(I(((E[0])+0.5*E[2]),E[1])-I(((E[0])-0.5*E[2]),E[1]))/(E[2])
    #return dIdv

#def ED(I,*E):
    #dIdv=(4*CD(I,E[0],E[1],(E[2]/2))-CD(I,E[0],E[1],(E[2])))/3
    #return dIdv
#def ex(v,T):
    #return(np.exp(v*T))

#def cd(I,v,T,h):
    #t1=v+0.5*h
    #t2=v-0.5*h
    #dIdv=(I(t1,T)-I(t2,T))/(h)


print(cd1(100000,1000,0.00001))
print(ed1(100000,1000,0.00001))
print(dI1(100000,1000))
    

