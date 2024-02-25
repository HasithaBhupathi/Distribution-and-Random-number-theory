import numpy as np
import matplotlib.pyplot as plt

#### create uniforn random numbers u~U(0,1)
N = 1000

x = np.zeros(N+1)
y = np.zeros(N+1)
u1 = np.zeros(N)
u2 = np.zeros(N)

z = np.zeros(N)   #### for standard normal distribution
X = np.zeros(N)   #### for normal distribution

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

#### normal distribution with mean = 4 and std = 2 ( peack occure near mean = 4)
  X[i] = z[i]*2+4

plt.hist(z,ec='white')
plt.title("Histrogram")
plt.show()
  
plt.hist(X,ec='white')
plt.title("Histrogram")
plt.show()

