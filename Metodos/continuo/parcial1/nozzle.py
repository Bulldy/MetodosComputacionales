import numpy as np
import matplotlib.pyplot as plt

def Area(x):
    a=1+2.2*((x-1.5)**2)
    return a

def p0x(x):
    p=1-0.3146*x
    return p

def T0x(x):
    t=1-0.2314*x
    return t

def V0x(x):
    v=(0.1+1.09*x)*((T0x(x))**0.5)
    return v

g=1.4
C=0.1
dx=0.1
tmax=20
xmax=3
xmin=0
Nx=int((xmax-xmin)/dx)+1
x=np.linspace(xmin,xmax,Nx)
t=[0]
rho=[]
T=[]
V=[]
A=[Area(i) for i in x]
rho.append([p0x(i) for i in x])
T.append([T0x(i) for i in x])
V.append([V0x(i) for i in x])
dts=[C*dx/((T[0][i]**0.5)+V[0][i]) for i in range(len(V[0]))]
dt=min(dts)
Nt=int(tmax/dt)
print(dt)

for j in range(Nt):
    t.append(t[j]+dt)
    rp=[]
    rp.append(1)
    tp=[]
    tp.append(1)
    vp=[]
    vp.append(V[j][0])
    for i in range(1,Nx-1):
        dp1=-(rho[j][i]/dx)*(V[j][i+1]-V[j][i])-(rho[j][i]*V[j][i]/dx)*(np.log(A[i+1])-np.log(A[i]))-(V[j][i]/dx)*(rho[j][i+1]-rho[j][i])
        dv1=-(V[j][i]/dx)*(V[j][i+1]-V[j][i])-(1/g)*(((T[j][i+1]-T[j][i])/dx)+(T[j][i]/rho[j][i])*(1/dx)*(rho[j][i+1]-rho[j][i]))
        dt1=-(V[j][i]/dx)*(T[j][i+1]-T[j][i])-(g-1)*(T[j][i]/dx)*((V[j][i+1]-V[j][i])+(V[j][i])*(np.log(A[i+1])-np.log(A[i])))
        ppp=rho[j][i]+dp1*dt
        vpp=V[j][i]+dv1*dt
        tpp=T[j][i]+dt1*dt
        rp.append(ppp)
        tp.append(tpp)
        vp.append(vpp)
    rn=[]
    tn=[]
    vn=[]
    rn.append(1)
    tn.append(1)
    for i in range(1,Nx-1):
        dp1=-(rho[j][i]/dx)*(V[j][i+1]-V[j][i])-(rho[j][i]*V[j][i]/dx)*(np.log(A[i+1])-np.log(A[i]))-(V[j][i]/dx)*(rho[j][i+1]-rho[j][i])
        dv1=-(V[j][i]/dx)*(V[j][i+1]-V[j][i])-(1/g)*(((T[j][i+1]-T[j][i])/dx)+(T[j][i]/rho[j][i])*(1/dx)*(rho[j][i+1]-rho[j][i]))
        dt1=-(V[j][i]/dx)*(T[j][i+1]-T[j][i])-(g-1)*(T[j][i]/dx)*((V[j][i+1]-V[j][i])+(V[j][i])*(np.log(A[i+1])-np.log(A[i])))

        dp2=-(rp[i]/dx)*(vp[i]-vp[i-1])-(rp[i]*vp[i]/dx)*(np.log(A[i])-np.log(A[i-1]))-(vp[i]/dx)*(rp[i]-rp[i-1])
        dpprom=0.5*(dp1+dp2)
        pnn=rho[j][i]+dpprom*dt
        rn.append(pnn)
        
        dv2=-(vp[i]/dx)*(vp[i]-vp[i-1])-(1/g)*(1/dx)*((tp[i]-tp[i-1])+(tp[i]/rp[i])*(rp[i]-rp[i-1]))
        dvprom=0.5*(dv1+dv2)
        vnn=V[j][i]+dvprom*dt
        vn.append(vnn)
        
        dt2=-(vp[i]/dx)*(tp[i]-tp[i-1])-(g-1)*(tp[i]/dx)*((vp[i]-vp[i-1])+(vp[i])*(np.log(A[i])-np.log(A[i-1])))
        dtprom=0.5*(dt1+dt2)
        tnn=T[j][i]+dtprom*dt
        tn.append(tnn)
        
    rul=2*rn[-1]-rn[-2]
    rn.append(rul)
    rho.append(rn)

    vi1=2*vn[0]-vn[1]
    vn.insert(0,vi1)
    vul=2*vn[-1]-vn[-2]
    vn.append(vul)
    V.append(vn)

    tul=2*tn[-1]-tn[-2]
    tn.append(tul)
    T.append(tn)


fig=plt.figure()
plo=[row[15] for row in rho]
plt.plot(t,plo)
plt.ylabel("Densidad adimensional")
plt.xlabel("Tiempo (s)")
plt.show()

fig=plt.figure()
plo=[row[15] for row in V]
plt.plot(t,plo)
plt.ylabel("Velocidad adimensional")
plt.xlabel("Tiempo (s)")
plt.show()

fig=plt.figure()
plo=[row[15] for row in T]
plt.plot(t,plo)
plt.ylabel("Temperatura adimensional")
plt.xlabel("Tiempo (s)")
plt.show()


