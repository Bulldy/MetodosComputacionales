import numpy as np
import matplotlib.pyplot as plt

def Area(x):
    a=1+2.2*((x-1.5)**2)
    return np.float128(a)

def p0x(x):
    p=1-0.3146*x
    return np.float128(p)

def T0x(x):
    t=1-0.2314*x
    return np.float128(t)

def V0x(x):
    v=(0.1+1.09*x)*((T0x(x))**0.5)
    return np.float128(v)

g=1.4
dt=0.0201
dx=0.1
tmax=10
Nt=int(tmax/dt)
xmax=3
xmin=0
Nx=int((xmax-xmin)/dx)+1
x=np.linspace(xmin,xmax,Nx)
t=[0]
rho=[]
T=[]
V=[]
A=[]
rho.append([p0x(i) for i in x])
T.append([T0x(i) for i in x])
V.append([V0x(i) for i in x])
A.append([Area(i) for i in x])
print(len(rho[0]),len(T[0]),len(V[0]),len(x))
print(Nx,Nt,len(x),len(A))
print(x[30])#[30],T[0][30],V[0][30],x[0][30])

for j in range(Nt):
    t.append(t[j]+dt)
    rhop=[]
    temp=[]
    velp=[]
    for i in range(1,Nx-1):
        dp1=-(rho[j][i]*(V[j][i+1]-V[j][i])/dx)-(rho[j][i]*V[j][i]*(np.log(A[i+1])-np.log(A[i]))/dx)-(V[j][i]*(rho[j][i+1]-rho[j][i])/dx)
        dv1=(-(V[j][i]*(V[j][i+1]-V[j][i])/dx)-(1/g)*(1/dx)*((T[j][i+1]-T[j][i])+(T[j][i]/rho[j][i])*(rho[j][i+1]-rho[j][i])))
        dt1=(-(V[j][i]*(T[j][i+1]-T[j][i])/dx)-(g-1)*(T[j][i]/dx)*((V[j][i+1]-V[j][i])+(V[j][i]*(np.log(A[i+1])-np.log(A[i])))))
        ppp=rho[j][i]+dp1*dt
        rhop.append(ppp)
        tpp=T[j][i]+dt1*dt
        temp.append(tpp)
        vpp=T[j][i]+dv1*dt
        velp.append(vpp)
    #print(
    rhon=[]
    tn=[]
    vn=[]
    rhon.append(1)
    tn.append(1)
    for i in range(1,Nx-2):
        dp1=(-(rho[j][i]*(V[j][i+1]-V[j][i])/dx)-(rho[j][i]*V[j][i]*(np.log(A(x[i+1]))-np.log(A(x[i])))/dx)-(V[j][i]*(rho[j][i+1]-rho[j][i])/dx))
        dv1=(-(V[j][i]*(V[j][i+1]-V[j][i])/dx)-(1/g)*(1/dx)*((T[j][i+1]-T[j][i])+(T[j][i]/rho[j][i])*(rho[j][i+1]-rho[j][i])))
        dt1=(-(V[j][i]*(T[j][i+1]-T[j][i])/dx)-(g-1)*(T[j][i]/dx)*((V[j][i+1]-V[j][i])+(V[j][i]*(np.log(A(x[i+1]))-np.log(A(x[i]))))))
        
        dp2=(-(rhop[i]*(velp[i]-velp[i-1])/dx)-(rhop[i]*velp[i]*(np.log(A(x[i]))-np.log(A(x[i-1])))/dx)-(velp[i]*(rhop[i]-rhop[i-1])/dx))
        dv2=(-(velp[i]*(velp[i]-velp[i-1])/dx)-(1/g)*(1/dx)*((temp[i]-temp[i-1])+(temp[i]/rhop[i])*(rhop[i]-rhop[i-1])))
        dt2=(-(velp[i]*(temp[i]-temp[i-1])/dx)-(g-1)*(temp[i]/dx)*((velp[i]-velp[i-1])+(velp[i]*(np.log(A(x[i]))-np.log(A(x[i-1]))))))
        
        dpprom=0.5*(dp1+dp2)
        dvprom=0.5*(dv1+dv2)
        dtprom=0.5*(dt1+dt2)
        
        pnn=np.longdouble(rho[j][i]+dpprom*dt)
        rhon.append(pnn)
        tnn=np.longdouble(T[j][i]+dtprom*dt)
        tn.append(tnn)
        vnn=np.longdouble(V[j][i]+dvprom*dt)
        vn.append(vnn)

    v0=2*vn[0]-vn[1]
    vn.insert(0,v0)
    vN=2*vn[-1]-vn[-2]
    vn.append(vN)
    pN=2*rhon[-1]-rhon[-2]
    rhon.append(pN)
    TN=2*tn[-1]-tn[-2]
    tn.append(TN)
    
    rho.append(np.array(rhon))
    V.append(np.array(vn))
    T.append(np.array(tn))
    #print(j)
#print(x)
#print(rho[0],rho[1])
#print(V[-1])

fig=plt.figure()
plo=[row[15] for row in rho]
plo2=[row[15] for row in V]
plt.scatter(t,plo)
plt.scatter(t,plo2)
plt.ylim([-2,2])
plt.show()
    
