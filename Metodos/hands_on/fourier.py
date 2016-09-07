import cmath as cm
import numpy as np
import matplotlib.pyplot as plt

N=1000
x=np.arange(0,2*np.pi,2*np.pi/N)
f=np.sin(x)
fg=[]

for k in range(N):
    ff=[]
    for n in range(len(f)):
        e=cm.exp(-2*cm.pi*1j*k*n/N)
        fk=f[n]*e
        ff.append(fk)
    fg.append(np.sum(ff))

#print(fg)

frecuencia=range(len(x))
re=[z.real for z in fg]
im=[z.imag for z in fg]

fig=plt.figure()
plt.scatter(frecuencia,re)
plt.scatter(frecuencia,im)
plt.show()
