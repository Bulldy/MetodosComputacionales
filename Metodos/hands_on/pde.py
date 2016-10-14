import numpy as np
import matplotlib.pyplot as plt

def u0x(x):
    return np.exp(-1*(x-2)**2)

L=10
dx=0.1
dt=0.05
c=0.5
T=10

Nx=int((L/dx))+1
Nt=int((T/dt))

x=np.linspace(0,L,Nx)
t=np.linspace(0,T,Nt)

u0=[u0x(i) for i in x]
u=[]
u.append(u0)

for j in range(Nt):
    una=[]
    for i in range(Nx):
        un=u[j][i]-(c*dt/dx)*(u[j][i]-u[j][i-1])
        una.append(un)
    u.append(una)

ulw=[]
ulw.append(u0)
alfa=c*dt/dx
bm1=(alfa/2)*(alfa+1)
b0=1-(alfa**2)
b1=(alfa/2)*(alfa-1)

for j in range(Nt):
    una=[]
    for i in range(Nx):
        if(i==Nx-1):
            un=bm1*ulw[j][i-1]+b0*ulw[j][i]+b1*ulw[j][0]
            una.append(un)
        elif(i!=Nx-1):
            un=bm1*ulw[j][i-1]+b0*ulw[j][i]+b1*ulw[j][i+1]
            una.append(un)
    ulw.append(una)

fig=plt.figure()
plt.plot(x,ulw[0])
plt.plot(x,ulw[-1])
plt.show()
