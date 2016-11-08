import cmath as cm
import numpy as np
import matplotlib.pyplot as plt

N=1000
x=np.arange(0,2*np.pi,2*np.pi/N)
f=np.sin(x)
fg=[]

for k in range(N):
    ff=[]
    for n in range(N):
        e=cm.exp(-2*cm.pi*1j*k*n/N)
        fk=f[n]*e
        ff.append(fk)
    fg.append(np.sum(ff))

#print(fg)

frecuencia=range(len(x))
re=[z.real for z in fg]
im=[z.imag for z in fg]

npfft=np.fft.fft(f)
fftt=[z.imag for z in npfft]

fig=plt.figure()
plt.stem(frecuencia,re,marker="|")
plt.stem(frecuencia,im,marker="|")
plt.xlim([-50,1050])
#plt.plot(frecuencia,fftt)
plt.show()


