import math
import numpy as np
import random

def f1(x):
    return ((np.exp(x))-10*x)

def f2(x):
    return (2*np.cos(x)-x)

def pi_f1(a,b):
    p1=random.uniform(a,b)
    p2=random.uniform(a,b)
    if (f1(p1)>0 and f2(p2)<0):
        return p1,p2
    while (f1(p1)<0 and f1(p2)>0):
        p1=random.uniform(a,b)
        p2=random.uniform(a,b)
        if (f1(p1)>0 & f2(p2)<0):
            return p1,p2

a,b=pi_f1(50,50)

print a,b
print f1(a),f1(b)
