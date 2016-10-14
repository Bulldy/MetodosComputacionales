import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import sys                                                                     

#Importar los datos de condiciones.dat
file=str(sys.argv[1])
data=[line.rstrip('\n') for line in open(file)]
N=int(data[0])
T=float(data[1])
m=float(data[2])
a=float(data[3])
y0=data[4]
y0=y0.split()
y0=[float(i) for i in y0]
yp0=data[5]
yp0=yp0.split()
yp0=[float(i) for i in yp0]
y0.insert(0,0)
yp0.insert(0,0)
y0.append(0)
yp0.append(0)

#Crear los arrays donde guardar los datos
y=[]
yp=[]
y.append(y0)
yp.append(yp0)
t=[0]
tmax=10
dt=0.1
Nt=int(tmax/dt)
nn=range(N+2)
energia=[]

#Encontramos energia inicial total
e0=0
for i in range(1,N+2):
    ec=0.5*m*((yp[0][i])**2)
    ep=0.5*(T/a)*((y[0][i]-y[0][i-1])**2)
    e0=e0+ec+ep
energia.append(e0)

#Solucionamos las ecuaciones de movimiento por medio de Leapfrog de segundo orden
for j in range(Nt):
    ej=0
    t.append(t[j]+dt)
    yt=np.zeros(N+2)
    yt=yt.tolist()
    ypt=np.zeros(N+2)
    ypt=ypt.tolist()
    for i in range(1,N+1):
        f=-1*(T/(m*a))*(2*y[j][i]-y[j][i-1]-y[j][i+1])
        yn1=y[j][i]+yp[j][i]*dt+0.5*f*(dt**2)
        yt[i]=yn1
    for i in range(1,N+1):
        f1=-1*(T/(m*a))*(2*y[j][i]-y[j][i-1]-y[j][i+1])
        f2=-1*(T/(m*a))*(2*yt[i]-yt[i-1]-yt[i+1])
        vn1=yp[j][i]+0.5*(f1+f2)*dt
        ypt[i]=vn1
    for i in range(1,N+2):
        ec=0.5*m*((ypt[i])**2)
        ep=0.5*(T/a)*((yt[i]-yt[i-1])**2)
        ej=ej+ec+ep
    y.append(yt)
    yp.append(ypt)
    energia.append(ej)

#Encontramos la variacion de la energia y la graficamos con respecto al tiempo
er=[((i-e0)*(1/e0)) for i in energia]

fig=plt.figure()
plt.plot(t,er)
plt.ylim([1.1*min(er),0.02])
plt.xlabel('Tiempo')
plt.ylabel('Variación de la energía total')
plt.savefig('energia.pdf')
plt.close()

#Creamos el GIF
mina=[min(a) for a in y]
minf=min(mina)
maxa=[max(a) for a in y]
maxf=max(maxa)
fig=plt.figure()
def actualizar(i):
    plt.cla()
    plt.plot(nn,y[i][:],'s-')
    plt.ylim(minf,maxf)
    plt.xlim(-1,max(nn)+1)
    plt.xlabel('Posicion de la masa')
    plt.ylabel('Amplitud del movimiento')
gif=ani.FuncAnimation(fig,actualizar,frames=Nt)
gif.save('movimiento.gif',writer='imagemagick',fps=3)
plt.close()
