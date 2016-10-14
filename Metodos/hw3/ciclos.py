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

dias=range(1,len(co)+1)

fig=plt.figure()
plt.plot(dias,no2)
plt.show()

import cmath as cm

def fourier(list):
    N=len(list)
    fc=[]
    e=cm.exp(-2*cm.pi*1j/N)
    for k in range(N):
        ff=[]
        for n in range(N):
            ekn=e**(k*n)
            fkn=list[n]*ekn
            ff.append(fkn)
        fc.append(np.sum(ff))
    return fc
    
fco=fourier(co)
fhc=fourier(hc)
fben=fourier(ben)
fnox=fourier(nox)
fno2=fourier(no2)

freq=range(len(co))
abs_fco=[abs(z) for z in fco]
abs_fhc=[abs(z) for z in fhc]
abs_fben=[abs(z) for z in fben]
abs_fnox=[abs(z) for z in fnox]
abs_fno2=[abs(z) for z in fno2]

fig=plt.figure()
plt.plot(freq,abs_fco)
plt.show()

fig=plt.figure()
plt.plot(freq,abs_fhc)
plt.show()

fig=plt.figure()
plt.plot(freq,abs_fben)
plt.show()

fig=plt.figure()
plt.plot(freq,abs_fnox)
plt.show()

fig=plt.figure()
plt.plot(freq,abs_fno2)
plt.show()

[3.2938645847209447, -458.92344452705441] [-42.710568968007841, -15.228165493872838] [-7.8986237727167659, -643.85681097285283] [3.4467473226436347, 235.06283600685325] [6.2032729769807213, -10.832717377994085]

[2.9797136539396192, 412.27405744979023] [14.451894017877168, 16.315499229771955] [595.03126990693363, 7.9964080858425826] [3.4704540043654997, 65.606326638847719] [5.8462731554457221, 6.3159596369553972]
