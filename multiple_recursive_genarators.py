import numpy as np
import matplotlib.pyplot as plt

N = 1000
k = 3

x = np.zeros(N+k,dtype='float')   #### x[i] belongs to the set {0,1,...,m-1}
u = np.zeros(N,dtype='float')     #### 0<=u[i]<1
a = np.zeros(k)                   #### a[i] belongs to the set {0,1,....m-1}
t = np.zeros(N)

m = (2**31)-1
       
a[0] = 7
a[1] = 78
a[2] = 125

x[0] = 48
x[1] = 1
x[2] = 12

for i in range(k,N+k):
  s = 0
  for r in range(1,k+1):
    s = s+a[r-1]*x[i-r]
  x[i] = s%m

for i in range(0,N):
  u[i] = x[k+i]/m

for i in range(0,N):
  t[i] = i+1


plt.plot(t,u,'o')
plt.show()
