import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt('data_A.txt')
x=data[:,0]
y=data[:,1]

Ex=np.mean(x)
Ey=np.mean(y)

sxx=np.mean(np.multiply(x-Ex,x-Ex))
sxy=np.mean(np.multiply(x-Ex,y-Ey))
syy=np.mean(np.multiply(y-Ey,y-Ey))
syx=np.mean(np.multiply(y-Ey,x-Ex))

cov=[[sxx,sxy],[syx,syy]]

print (cov)
