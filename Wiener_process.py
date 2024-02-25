import numpy as np
import matplotlib.pyplot as plt

####          wiener process

#### generate uniform random numbers
N = 101

x = np.zeros(N+1)
y = np.zeros(N+1)
u1 = np.zeros(N)
u2 = np.zeros(N)

z = np.zeros(N)   #### for standard normal distribution

x[0] = 100
y[0] = 10
m1 = (2**32)-1
m2 = (2**32)-1157

for i in range(0,N):
  x[i+1] = (170*x[i])%m1
  y[i+1] = (172*y[i])%m2

  u1[i] = x[i+1]/m1
  u2[i] = y[i+1]/m2
  
#### standard Normal distributions by box-muller approach ( peack occure near mean = 0)
  z[i] = ((-2*np.log(u1[i]))**0.5)*np.sin(2*np.pi*u2[i])  #### we can use both sin or cosin

#### generate the time interval
t = np.zeros(N)
for i in range(1,N):
    t[i] = t[0]+0.01*i

#### generate wiener values
w = np.zeros(N)
for i in range(1,N):
    s = 0
    for j in range(1,i+1):
        s = s+z[j]
    w[i] = (t[i]-t[i-1])**0.5*s

plt.plot(t,w)
plt.show()
