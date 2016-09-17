import numpy as np
import scipy.constants as sc
import mpmath

mpmath.mp.dps=150

#Plancks law function (I(v,T)) and its derivatives are defined
def I(v,T):
    k=((2*sc.h/(sc.c**2)))*(v**3)
    d=(1/(mpmath.expm1((sc.h*v/(sc.k*T)))))
    return mpmath.mpf(k*d)

def cd1(v,T,h):
    c=(I(v+0.5*h,T)-I(v-0.5*h,T))/h
    return mpmath.mpf(c)

def dI1(v,T,h):
    d=(4*cd1(v,T,0.5*h)-cd1(v,T,h))/3
    return mpmath.mpf(d)

def cd2(v,T,h):
    c=(dI1(v+0.5*h,T,h)-dI1(v-0.5*h,T,h))/h
    return mpmath.mpf(c)

def dI2(v,T,h):
    d=(4*cd2(v,T,0.5*h)-cd2(v,T,h))/3
    return mpmath.mpf(d)

#The temperature space is defined
T=np.logspace(0,9)

#Newton-Raphson begins, its parameters are stated
tol=mpmath.mpf(1e-70)
maxiter=1000
b=[]
h=mpmath.mpf(1e-35)
h1=mpmath.mpf(1e-50)

#Newton Raphson
for t in T:
    v0=mpmath.mpf(3.5e10*t)
    for i in range(maxiter):
        F=dI1(v0,t,h)
        if(abs(F)<tol):
            b.append(v0/t)
            break
        v0=v0-(F/(dI2(v0,t,h1)))

#We find the mean for the b vector
b_dat=float(mpmath.fsum(b)/len(b))/(1.0e9)

#We save b in a .dat file
f=open('b.dat','w')
f.write(str(b_dat))
f.close()
