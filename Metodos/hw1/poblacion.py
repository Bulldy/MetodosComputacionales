import numpy as np
import matplotlib.pyplot as plt
import genetica
import scipy.special as ssp

N=200
rpob=[]
ppob=[]
ll=[]

for i in range(N+1):
    r=genetica.Expresion()
    r.resuelve()
    rpob.append(r.r[-1])
    ppob.append(r.p[-1])
    ll.append((r.kr/r.yr))

l=ll[-1]

file_r=open("r_poblacion.dat","w")
for i in range(len(rpob)):
    file_r.write("%f \n" %rpob[i])
file_r.close()

file_p=open("p_poblacion.dat","w")
for i in range(len(ppob)):
    file_p.write("%f \n" %ppob[i])
file_p.close()

figr=plt.figure()
r=np.arange(0,max(rpob),0.1)
one=np.ones(len(r))
Pr=np.divide((np.power(l,r))*np.exp(-l),(ssp.gamma(np.add(r,one))))
n,b,p=plt.hist(rpob,bins=range(0,int(max(rpob))+1),normed=True)
plt.plot(r,Pr,label="Poisson")
ax=plt.axes()
ax.set_xlabel("Numero de ARNm")
ax.set_ylabel("Frecuencia Normalizada")
plt.legend()
filer = 'r_histograma' 
plt.savefig(filer+'.pdf',format = 'pdf')
plt.close()

figp=plt.figure()
n,p,b=plt.hist(ppob,bins=int(np.sqrt(len(ppob))),normed=True)
ax=plt.axes()
ax.set_xlabel("Numero de proteinas")
ax.set_ylabel("Frecuencia Normalizada")
filep='p_histograma'
plt.savefig(filep+'.pdf',format='pdf')
plt.close()


    
