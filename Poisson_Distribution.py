import numpy as np
import math
import matplotlib.pyplot as plt

#### generate uniform random numbers
N = 1000
x = np.zeros(N+1)
u = np.zeros(N)

x[0] = 100
m = 2**31-1
c = 0
a = 137

for i in range(0,N):
    x[i+1] = (a*x[i]+c)%m
    u[i] = x[i+1]/m

#### generate poisson values    
lam = 0.7
n = 1
b = 1
O = []

for i in range(0,N):
    b =b*u[i]
    if b>=math.exp(-1*lam):
        n = n+1
    else:
        p = n-1
        O.append(p)
        b = 1
        n = 1
    if len(O)>=100:
       break
    
plt.hist(O,ec='red')
plt.show()
