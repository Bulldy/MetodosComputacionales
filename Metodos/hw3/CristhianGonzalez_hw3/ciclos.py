import numpy as np
import matplotlib.pyplot as plt
import sys
import csv

file=str(sys.argv[1])

#Cambiamos los puntos por comas e importamos los datos
with open(file,'r') as f:
    data=f.read()
data=data.replace(',','.')
data=data.replace(';;','')
with open(file,'w') as f:
    f.write(data)

data=np.loadtxt(file,delimiter=';',skiprows=1,usecols={4,5,7,9,2})

#Obtenemos los datos y los -200 por ahora los volvemos nan
#Obviamos el primer y ultimo dia, que no estan completos
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

#Para cada dia tomamos el promedio de 0 h a 24 h, asi tenemos un muestreo por dias
#Para hacer el promedio omitimos nan
for i in range(23,len(no2h)+23,24):
    co.append(np.nanmean(coh[(i-23):i]))
    hc.append(np.nanmean(hch[(i-23):i]))
    ben.append(np.nanmean(bh[(i-23):i]))
    nox.append(np.nanmean(noxh[(i-23):i]))
    no2.append(np.nanmean(no2h[(i-23):i]))

#Como primera aproximacion convertimos los nan en 0
#Como interpolacion gruesa, tomamos el maximo de los valores y lo multiplicamos por aleatorio
coo=max(co)
co=np.nan_to_num(co)
for i in range(len(co)):
    if(co[i]==0):
        co[i]=np.random.random()*coo
hc=hc[:55]
hco=max(hc)
hc=np.nan_to_num(hc)
for i in range(len(hc)):
    if(hc[i]==0):
        hc[i]=np.random.random()*hco
beno=max(ben)
ben=np.nan_to_num(ben)
for i in range(len(ben)):
    if(ben[i]==0):
        ben[i]=np.random.random()*beno
noxo=max(nox)
nox=np.nan_to_num(nox)
for i in range(len(nox)):
    if(nox[i]==0):
        nox[i]=np.random.random()*noxo
no2o=max(no2)
no2=np.nan_to_num(no2)
for i in range(len(no2)):
    if(no2[i]==0):
        no2[i]=np.random.random()*no2o

#Hacemos analisis de fourier
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
fco=fco[1:int(len(co)/2)]
fhc=fourier(hc)
fhc=fhc[1:int(len(hc)/2)]
fben=fourier(ben)
fben=fben[1:int(len(ben)/2)]
fnox=fourier(nox)
fnox=fnox[1:int(len(nox)/2)]
fno2=fourier(no2)
fno2=fno2[1:int(len(no2)/2)]

#Como criterio para escoger periodos dominantes, comparamos las magnitudes en la transformada
freq=range(1,len(fco)+1)
freq1=range(1,len(fhc)+1)
abs_fco=[abs(z) for z in fco]
abs_fhc=[abs(z) for z in fhc]
abs_fben=[abs(z) for z in fben]
abs_fnox=[abs(z) for z in fnox]
abs_fno2=[abs(z) for z in fno2]
wco=[cm.phase(z) for z in fco]
whc=[cm.phase(z) for z in fhc]
wben=[cm.phase(z) for z in fben]
wnox=[cm.phase(z) for z in fnox]
wno2=[cm.phase(z) for z in fno2]

ico=[]
iico=np.argsort(abs_fco)
ico.append(iico[-1])
ico.append(iico[-2])
ihc=[]
iihc=np.argsort(abs_fhc)
ihc.append(iihc[-1])
ihc.append(iihc[-2])
iben=[]
iiben=np.argsort(abs_fben)
iben.append(iiben[-1])
iben.append(iiben[-2])
inox=[]
iinox=np.argsort(abs_fnox)
inox.append(iinox[-1])
inox.append(iinox[-2])
ino2=[]
iino2=np.argsort(abs_fno2)
ino2.append(iino2[-1])
ino2.append(iino2[-2])

#Hallamos los periodos en dias
Tco=[abs(2*np.pi*(k+1)/(wco[k])) for k in ico]
Thc=[abs(2*np.pi*(k+1)/(whc[k])) for k in ihc]
Tben=[abs(2*np.pi*(k+1)/(wben[k])) for k in iben]
Tnox=[abs(2*np.pi*(k+1)/(wnox[k])) for k in inox]
Tno2=[abs(2*np.pi*(k+1)/(wno2[k])) for k in ino2]
T=np.stack((Tco,Thc,Tben,Tnox,Tno2))
np.savetxt('periodos.dat',T)



