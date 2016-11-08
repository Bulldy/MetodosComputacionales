import random 
import numpy as np

nh=0
N=10**7
x=random.random()
y=random.random()
d=0.1

for i in range(N):
    px=np.random.uniform(-1*d,d)
    py=np.random.uniform(-1*d,d)
    if(abs(x+px)<1 and abs(y+py)<1):
        x=x+px
        y=y+py
    if(x**2+y**2<1):
        nh=nh+1

print(nh*4/N)
