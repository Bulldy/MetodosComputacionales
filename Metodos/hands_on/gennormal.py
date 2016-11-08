import random
import matplotlib.pyplot as plt

num=[]
N=10000

for j in range(N):
    ran=0
    for i in range(N):
        ran=ran+random.random()
    num.append(ran)
num=[(i-N/2) for i in num] 

plt.hist(num,50)
plt.show()
