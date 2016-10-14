import numpy as np
import sys
import StringIO as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = open(sys.argv[1], 'r')
valores= data.readlines()

N_data= int(valores[0])
T_data= float(valores[1])
m_data= float(valores[2])
a_data= float(valores[3])
y0_data= valores[4].split(" ")
v0_data= valores[5].split(" ")

for i in range (len(y0_data)):
	y0_data[i]=float(y0_data[i])
	v0_data[i]=float(v0_data[i])

y0_data= np.array(y0_data)
v0_data= np.array(v0_data)


#print(type(data))
#print (N_data)
#print (T_data)
#print (m_data)
#print (a_data)
#print (y0_data)
#print (v0_data)


#N_data= 5
#T_data= 5.0
#m_data= 1.0
#a_data= 2.0
#y0_data= [3.5, 4.2, 5.4, 1.3, 3.8]
#v0_data= [2.3, 4.5, 6.3, 4.1, 6.7]

tf= 10.0
dt= 0.1

def LeapFrog_2orden (N= N_data, T= T_data, m= m_data, t_final= tf, a= a_data, delta_t= dt,  y_0= y0_data, yprime_0= v0_data):

	# N es el numero de masas, condandolas desde 0 

	y_matriz = np.zeros(((t_final/delta_t), N+2))
	v_matriz = np.zeros(((t_final/delta_t), N+2))

	y_matriz[0,1:-1]= y_0
	y_matriz[:,0]= 0.0
	y_matriz[:,-1]= 0.0


	v_matriz[0,1:-1]= yprime_0
	v_matriz[:,0]= 0.0
	v_matriz[:,-1]= 0.0


	# Matriz de posicion y velovidad en el primer paso de delta_t
	y_matriz[1,1:-1]= y_matriz[0,1:-1] + v_matriz[0,1:-1]*delta_t
	v_matriz[1,1:-1]= v_matriz[0,1:-1] + -T/(m*a)*(2*y_matriz[0,1:-1]- y_matriz[0, 0:-2]- y_matriz[0, 2:])*delta_t

	for i in range (2, int(t_final/delta_t)):
		k_y= v_matriz[i-1,1:-1]
		k_v= -T/(m*a)*(2*y_matriz[i-1,1:-1]- y_matriz[i-1, 0:-2]- y_matriz[i-1, 2:]) 
		y_matriz[i,1:-1] = y_matriz[i-2, 1:-1] + k_y * delta_t *2.0
		v_matriz[i,1:-1] = v_matriz[i-2, 1:-1] + k_v * delta_t *2.0


	return y_matriz, v_matriz

 
#Gif
x_space= np.arange(0,N_data+2,1)
y_pos, y_vel = LeapFrog_2orden()

def animate(nframe):
	#para limpiar la figura
	plt.cla()
	plt.plot(x_space, y_pos[nframe,:], 'o-')
	plt.ylim(y_pos.min(), y_pos.max())
	plt.xlim(0, N_data+1)

fig= plt.figure(figsize=(6,5))

anim = animation.FuncAnimation (fig, animate, frames=len(y_pos))
anim.save('movimiento.gif', writer='imagemagick', fps= 3)


# Energia 
t= np.arange (0, tf, dt)

Ek_0= (1.0/2.0)*m_data*np.sum(y_vel[0,:])**2
Eu_0= (1.0/2.0)*(T_data/a_data)*np.sum(y_pos[0,:]**2) 


Ek= (1.0/2.0)*m_data*np.sum(y_vel**2, axis=1)
Eu= (1.0/2.0)*(T_data/a_data)*np.sum(y_pos**2, axis=1)  
  

TOTAL_E0= Ek_0 + Eu_0
TOTAL_E= Ek + Eu

#Arreglo de la variacion de la energia total del sistema respecto a la energia inicial	
E= abs(TOTAL_E - TOTAL_E0)/TOTAL_E0

#Grafica variacion energia total del sistema	
plt.figure()
plt.plot(t, E)
plt.title('Variacion de la energia total del sistema')	
plt.ylabel('E(t)-E0 / E0')
plt.xlabel('time')
plt.savefig("energia.pdf", format='pdf')


