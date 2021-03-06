import numpy as np
import matplotlib.pyplot as plt
import sys
#from images2gif import writeGif
#import PIL

file=str(sys.argv[1])

data=[line.rstrip('\n') for line in open(file)]

N=int(data[0])+2
T=float(data[1])
m=float(data[2])
a=float(data[3])
y0=data[4]
y0=y0.split()
y0=np.array([float(i) for i in y0])
yp0=data[5]
yp0=yp0.split()
yp0=np.array([float(i) for i in yp0])


y=[[i] for i in y0]
yp=[[i] for i in yp0]
y.append([0])
y.insert(0,[0])
yp.append([0])
yp.insert(0,[0])
tmax=10
dt=0.0001
pasos=int(tmax/dt)+1
t=[0]
nn=range(0,N)
imagenes=[]
energia=[]
e0=0
for n in range(1,N):
    ec=0.5*m*(yp[n][0])**2
    ep=0.5*(T/a)*((y[n][0]-y[n-1][0])**2)
    e0=e0+ec+ep
energia.append(e0)

for j in range(pasos-1):
    ej=0
    t.append(t[j]+dt)
    yp[0].append(0)
    yp[-1].append(0)
    y[0].append(0)
    y[-1].append(0)
    for n in range(1,N-1):
        ypp=-1*(T/(m*a))*(2*yp[n][j]-yp[n-1][j]-yp[n+1][j])
        yp12=yp[n][j]+ypp*dt*0.5
        ynn=y[n][j]+yp12*dt
        ypp12=-1*(T/(m*a))*(2*yp12-yp[n-1][j]-yp[n+1][j])
        ypnn=yp12+ypp12*dt*0.5
        yp[n].append(ypnn)
        y[n].append(ynn)
        ec=0.5*m*(yp[n][j])**2
        ep=0.5*(T/a)*((y[n][j]-y[n-1][j])**2)
        ej=ej+ec+ep
    eup=0.5*(T/a)*((y[-2][j])**2)
    ej=ej+eup
    energia.append(ej)


er=(energia-e0)*(1/e0)

#print(yp[0])
print(len(y[1]))
print(len(t))

fig=plt.figure()
plt.plot(t,y[int(len(y)/2)])
plt.plot(t,y[1])
plt.plot(t,y[-2])
plt.plot(t,y[-1])
plt.plot(t,y[0])
#plt.show()

fig=plt.figure()
plt.plot(t,er)
plt.xlabel('Tiempo (s)')
plt.ylabel('Variacion de la energia total')
fil='energia.pdf'
plt.savefig(fil,format='pdf')
#plt.show()

for j in range(1):
    ej=0
    t.append(t[j]+dt)
    yt=np.zeros(N+2)
    yt=yt.tolist()
    ypt=np.zeros(N+2)
    ypt=ypt.tolist()
    for i in range(1,N+1):
        f=-1*(T/(m*a))*(2*y[j][i]-y[j][i-1]-y[j][i+1])
        vn12=yp[j][i]+0.5*f*dt
        yn1=y[j][i]+dt*vn12
        yt[i]=yn1
    for i in range(1,N+1):
        f=-1*(T/(m*a))*(2*yt[i]-yt[i-1]-yt[i+1])
        vn12=yp[j][i]+0.5*f*dt
        vn1=vn12+0.5*dt*f
        ypt[i]=vn1
    for i in range(1,N+2):
        ec=0.5*m*((ypt[i])**2)
        ep=0.5*(T/a)*((yt[i]-yt[i-1])**2)
        ej=ej+ec+ep
    y.append(yt)
    yp.append(ypt)
    energia.append(ej)
