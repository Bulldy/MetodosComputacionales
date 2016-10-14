import numpy as np
import matplotlib.pyplot as plt

rho=28
s=10
beta=8.0/3.0

def dx(x,y,z):
    return s*(y-x)

def dy(x,y,z):
    return (x*(rho-z)-y)

def dz(x,y,z):
    return (x*y-beta*z)

tmin=0
tmax=40
dt=0.01
N=int((tmax-tmin)/dt)
x=[]
x.append(2.0)
y=[]
y.append(3.0)
z=[]
z.append(4.0)
t=[]
t.append(0)

#Metodo Runge Kutta 2
for i in range(N):
    t12=t[i]+0.5*dt
    x12=x[i]+0.5*dt*dx(x[i],y[i],z[i])
    y12=y[i]+0.5*dt*dy(x[i],y[i],z[i])
    z12=z[i]+0.5*dt*dz(x[i],y[i],z[i])
    xa=x[i]+dt*dx(x12,y12,z12)
    ya=y[i]+dt*dy(x12,y12,z12)
    za=z[i]+dt*dz(x12,y12,z12)
    x.append(xa)
    y.append(ya)
    z.append(za)
    t.append(t[i]+dt)


fig1=plt.figure()
plt.plot(y,x)
plt.ylabel('x')
plt.xlabel('y')
plt.show()

fig2=plt.figure()
plt.plot(z,x)
plt.xlabel('z')
plt.ylabel('x')
plt.show()

fig3=plt.figure()
plt.plot(z,y)
plt.xlabel('z')
plt.ylabel('y')
plt.show()

    







