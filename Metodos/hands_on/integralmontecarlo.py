import math
import random
import numpy as np

x=[]
N=10000
b=1
a=0

for i in range(N):
    r=random.random()
    np.append(x,r)

f=np.exp(x)
fp=np.mean(f)

inte=(b-a)*fp

print inte


