import numpy as np
import matplotlib.pyplot as plt
import math

def UV(N):
    global u,v
    x = np.zeros(N+1)
    y = np.zeros(N+1)

    u = np.zeros(N)
    v = np.zeros(N)

    a = 7**5
    c = 0
    m = 2**31-1
    x[0] = 100
    y[0] = 10

    for i in range(0,N):
        x[i+1] = (a*x[i]+c)%m
        y[i+1] = (a*y[i]+c)%m

        u[i] = x[i+1]/m
        v[i] = y[i+1]/m

N = 1000
UV(N)

x = [1,2,3,4,5,6]
p = [2/50,11/50,23/50,9/50,4/50,1/50]
n = len(p)

q = []
for i in range(0,n):
    q.append(n*p[i])

l = []
g = []

for i in range(0,n):
    if q[i]<1:
        l.append(x[i])
    else:
        g.append(x[i])

a = np.zeros(n)

while (len(g)!=0)and(len(l)!=0):
    i = min(l)
    j = max(g)
    a[i-1] = j
    q[j-1] = q[j-1]-(1-q[i-1])
    
    if q[j-1]<1:
        g.remove(j)
        l.append(j)

    l.remove(i)
    
out = np.zeros(N)

for i in range(0,N):
    k = math.ceil(u[i]*n)-1

    if v[i]>q[k]:
        out[i] = a[k]
    else:
        out[i] = k+1

bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5]
plt.hist(out,bins = bins,ec='black')
plt.title("Alias method")
plt.show()
        
    
        

