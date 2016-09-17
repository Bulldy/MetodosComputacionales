import numpy as np
import scipy.constants as sc
import mpmath

mpmath.mp.dps=50

#El valor de C fue econtrado al resolver analiticamente la ecuacion:
#e^C(64-16C)-64=0 
C=3.92069
def fz(z):
    e=1/(mpmath.expm1(z*C/(1-z)))
    a=(z**3)/((1-z)**5)
    return mpmath.mpf(e*a)

#Integramos usando el metodo de Simpson
N=1001
h=1.0/N
iz=0

for k in range(N):
    if(k==0):
        iz=iz
    elif(k==(N-1)):
        iz=iz+fz(k*h)
    elif(k%2==0):
        iz=iz+fz(k*h)*2
    elif(k%2==1):
        iz=iz+fz(k*h)*4

iz=(h/3.0)*iz
ix=sc.pi*((sc.k/sc.h)**4)*(2*sc.h/(sc.c**2))*(C**4)*iz

print(sc.physical_constants["Stefan-Boltzmann constant"][0])
print(float(ix))
