import numpy as np
import matplotlib.pyplot as plt

def poisson_process(n,lambd):
    x = np.zeros(n+1)
    
    u = np.zeros(n)
    v = np.zeros(n)
    w = np.zeros(n)
    
    x[0] = 101
    a = 7**5
    c = 10
    m = 2**31-1

    for i in range(0,n):
        x[i+1] = (a*x[i]+c)%m

        u[i] = x[i+1]/m
        v[i] = -np.log(u[i])/lambd
        w[i] = sum(v[0:i+1])

    return w
        
lambd = 0.8
n = 20

plt.step(poisson_process(n,lambd),range(1,n+1),where='post',marker='o')
plt.xlim([0,25])
plt.show()
