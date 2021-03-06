import numpy as np
import scipy.constants as sc
import mpmath

mpmath.mp.dps=150

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

T=np.logspace(0,9)
tol=mpmath.mpf(1e-70)
maxiter=100000
b=[]
h=mpmath.mpf(1e-35)
h1=mpmath.mpf(1e-50)

for t in T:
    v0=mpmath.mpf(4e10*t)
    for i in range(maxiter):
        F=dI1(v0,t,h)
        #print(F)
        #print(t)
        if(abs(F)<tol):
            b.append(v0/t)
            break
        v0=v0-(F/(dI2(v0,t,h1)))


print(sc.physical_constants["Wien frequency displacement law constant"][0])
print(float(mpmath.fsum(b)/len(b)))

