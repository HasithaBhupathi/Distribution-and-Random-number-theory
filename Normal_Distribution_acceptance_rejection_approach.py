import numpy as np
import matplotlib.pyplot as plt

#### create uniform distribution u~U(0,1)
N = 10000
x = np.zeros(N+1)
y = np.zeros(N+1)
z = np.zeros(N+1)

u = np.zeros(N)
v = np.zeros(N)
w = np.zeros(N)

x[0] = 10
y[0] = 111
z[0] = 19

a1 = 117
a2 = 118
a3 = 111

m1 = 2**31-1
m2 = 2**29-1
m3 = 2**33-1

c = 0

for i in range(0,N):
    x[i+1] = (a1*x[i]+c)%m1
    y[i+1] = (a2*y[i]+c)%m2
    z[i+1] = (a3*z[i]+c)%m3
    
    u[i] = x[i+1]/m1
    v[i] = y[i+1]/m2
    w[i] = z[i+1]/m3
    
#### generator acceptance-rejection from Exp(1)
e = np.zeros(N)
I = np.zeros(N)
op = np.zeros(N)
lam = 1

#### Standard normal distribution X~N(0,1)
for i in range(0,N):
    e[i] = -np.log(v[i])
    if w[i]<=0.5:
        I[i] = 1
    if u[i]<=np.exp(-((e[i]-1)**2)/2):
        op[i] = (1-2*I[i])*e[i]

#### Normal distribution X~N(a,b) a = mean b = standard deviasion
o = []
a = 4
b = 2
for i in range(0,N):
    o.append(op[i]*b+a)
      
plt.hist(op,ec='white')
plt.show()

plt.hist(o,ec='white')
plt.show()

    
    
    
    
    
