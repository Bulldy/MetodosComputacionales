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
hco=max(hc)
hc=np.nan_to_num(hc)
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

#Para arreglar el problema de las unidades cambiamos todo a ug/m^3
co=co*1000 #mg/m^3 de CO a ug/m3
nox=nox*(150/100) #ppb NOx a ug/m^3 (Highway Pollution edited by R.S. Hamilton, R.M. Harrison) Pag 7

data=np.stack((co,hc,ben,nox,no2),axis=-1)

#Encontramos valores esperados
Exi=[]
shape=data.shape
dims=shape[1]
for i in range(dims):
    x=data[:,i]
    ex=np.mean(x)
    Exi.append(ex)

#Encontramos matriz de covarianza y vectores y valores propios
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

#Encontramos proyeccion de los datos sobre vectores principales
d1=np.dot(v1.T,data.T)
d2=np.dot(v2.T,data.T)
d3=np.dot(v3.T,data.T)
d4=np.dot(v4.T,data.T)
d5=np.dot(v5.T,data.T)
d=np.stack((d1,d2),axis=-1)
np.savetxt('pca.dat',d)

#Graficamos valores con respecto a los dos componentes principales
fig=plt.figure()
plt.scatter(d1,d2)
plt.xlabel('Primer componente principal')
plt.ylabel('Segundo componente principal')
plt.savefig('pca.pdf',format='pdf')
plt.close()

#Encontramos la varianza 
var1=np.var(d1)
var2=np.var(d2)
var3=np.var(d3)
var4=np.var(d4)
var5=np.var(d5)
vart=var1+var2+var3+var4+var5
vr1=(var1/vart)*100
vr2=(var2/vart)*100
v=np.stack((vr1,vr2),axis=-1)
np.savetxt('varianza.dat',v)
