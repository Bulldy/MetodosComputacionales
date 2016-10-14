import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=1.0

def d2(theta):
    return (-1*g/l)*np.sin(theta)

tmin=0
tmax=10
dt=0.0001 #Aca se cambia para dt=0.05
N=int((tmax-tmin)/dt)
t=[]
t.append(tmin)
dtheta_0=0
dtheta=[]
dtheta.append(dtheta_0)
theta_0=np.pi/4
theta=[]
theta.append(theta_0)

#Metodo Euler
for i in range(N):
    dth=dtheta[i]+d2(theta[i])*dt
    dtheta.append(dth)
    th=theta[i]+dtheta[i]*dt
    theta.append(th)
    t.append(t[i]+dt)

theta=[t*180/np.pi for t in theta]
fig=plt.figure()
plt.rc('text',usetex=True)
plt.plot(t,theta, label='Metodo Euler')
plt.plot(t,theta_0*(180/np.pi)*np.cos(((g/l)**0.5)*np.array(t)),label='Aproximacion Lineal')
plt.legend(loc=2)
plt.xlabel(r'Tiempo (s)')
plt.ylabel(r'$\theta (t)$'+' (Grados)$')
plt.show()
