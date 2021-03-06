import numpy as np
import matplotlib.pyplot as plt
import sys
import csv

file=str(sys.argv[1])

with open(file,'r') as f:
    data=f.read()
data=data.replace(',','.')
data=data.replace(';;','')
with open(file,'w') as f:
    f.write(data)

data=np.loadtxt(file,delimiter=';',skiprows=1,usecols={4,5,7,9,2})

no2h=data[:,0]
no2h=no2h[7:(len(no2h)-14)]
no2h[no2h<0]=np.nan
coh=data[:,1]
coh=coh[7:(len(coh)-14)]
coh[coh<0]=np.nan
hch=data[:,2]
hch=hch[7:(len(hch)-14)]
hch[hch<0]=np.nan
bh=data[:,3]
bh=bh[7:(len(bh)-14)]
bh[bh<0]=np.nan
noxh=data[:,4]
noxh=noxh[7:(len(noxh)-14)]
noxh[noxh<0]=np.nan
co=[]
hc=[]
ben=[]
nox=[]
no2=[]

for i in range(23,len(no2h)+23,24):
    co.append(np.nanmean(coh[(i-23):i]))
    hc.append(np.nanmean(hch[(i-23):i]))
    ben.append(np.nanmean(bh[(i-23):i]))
    nox.append(np.nanmean(noxh[(i-23):i]))
    no2.append(np.nanmean(no2h[(i-23):i]))

co=np.nan_to_num(co)
co[co==0]=np.random.random()*np.nanmean(co)
hc=np.nan_to_num(hc)
ben=np.nan_to_num(ben)
ben[ben==0]=np.random.random()*np.nanmean(ben)
nox=np.nan_to_num(nox)
nox[nox==0]=np.random.random()*np.nanmean(nox)
no2=np.nan_to_num(no2)
no2[no2==0]=np.random.random()*np.nanmean(no2)

nox=nox*(0.150/100) #ppb NOx a mg/m^3

data=np.stack((co,hc,ben,nox,no2),axis=-1)

Exi=[]
shape=data.shape
dims=shape[1]

for i in range(dims):
    x=data[:,i]
    ex=np.mean(x)
    Exi.append(ex)

sij=[]

for i in range(dims):
    for j in range(dims):
        s=np.mean(np.multiply(data[:,i]-Exi[i],data[:,j]-Exi[j]))
        sij.append(s)

cov=np.reshape(sij,(dims,dims))

l,v=np.linalg.eig(cov)

idx = l.argsort()[::-1]   
l=l[idx]
v= v[:,idx]

v1=v[:,0]
v2=v[:,1]
v3=v[:,2]
v4=v[:,3]
v5=v[:,4]

d1=np.dot(v1.T,data.T)
d2=np.dot(v2.T,data.T)
d3=np.dot(v3.T,data.T)
d4=np.dot(v4.T,data.T)
d5=np.dot(v5.T,data.T)
d=np.stack((d1,d2),axis=-1)
np.savetxt('pca.dat',d)

fig=plt.figure()
plt.scatter(d2,d1)
plt.xlabel('Primer componente principal')
plt.ylabel('Segundo componente principal')
plt.savefig('pca.pdf',format='pdf')
plt.show()

var1=np.var(d1)
var2=np.var(d2)
var3=np.var(d3)
var4=np.var(d4)
var5=np.var(d5)
vart=var1+var2+var3+var4+var5

vr1=var1/vart
vr2=var2/vart
v=np.stack((vr1,vr2),axis=-1)
np.savetxt('varianza.dat',v)

