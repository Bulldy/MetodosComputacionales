import numpy as np
import matplotlib.pyplot as plt



def dy(y,t):
    return -1*y

#Intervalo 0<t<5
tmin=0
tmax=5
N=500
y=[]
y0=1
y.append(y0)
dt=(tmax-tmin)/N
t=[]
t.append(tmin)

#Metodo Euler
for i in range(N):
    yn=y[i]+dy(y[i],t[i])*dt
    y.append(yn)
    t.append(t[i]+dt)

#Metodo Leapfrog
ylp=[]
ylp.append(y0)
ylp1=ylp[0]+dy(y[0],t[0])*dt
ylp.append(ylp1)
for n in range(1,N):
    yn1=y[n-1]+2*dt*dy(y[n],t[n])
    ylp.append(yn1)

#Metodo Runge-Kutta 2
yrk2=[]
yrk2.append(y0)
for n in range(N):
    yn12=y[n]+dy(y[n],t[n])*0.5*dt
    tn12=(t[n]+0.5*dt)
    yn1=y[n]+dy(yn12,tn12)*dt
    yrk2.append(yn1)

#Metodo Runge-Kutta 4
yrk4=[]
yrk4.append(y0)
for n in range(N):
    k1=dy(y[n],t[n])
    k2=dy(y[n]+0.5*dt*k1,t[n]+0.5*dt)
    k3=dy(y[n]+0.5*dt*k2,t[n]+0.5*dt)
    k4=dy(y[n]+0.5*dt*k3,t[n]+dt)
    k=(k1+2*k2+2*k3+k4)/(6.0)
    yn1=y[n]+dt*k
    yrk4.append(yn1)


#Analitica
yy=np.exp(-1*np.array(t))

difeuler=abs(y-yy)
diflp=abs(ylp-yy)
difrk2=abs(yrk2-yy)
difrk4=abs(yrk4-yy)

fig=plt.figure()
plt.plot(t,difeuler,label='Euler')
plt.plot(t,diflp,label='Leap Frog')
plt.plot(t,difrk2,label='RK-2')
plt.plot(t,difrk4,label='RK-4')
plt.legend()
plt.show()
    

