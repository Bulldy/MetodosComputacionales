import random
import math
import matplotlib.pyplot as plt
x=[]
y=[]
N=1000

for i in range(N):
    s=5
    p=random.random(0,2*math.pi)
    l=-1*math.log(random.random())
    r=s*(2*l)**0.5
    xx=r*math.cos(p)
    yy=r*math.sin(p)
    x.append(xx)
    y.append(yy)

fig1=plt.figure()
plt.hist(x,50)

fig2=plt.figure()
plt.hist(y,50)
plt.show()
