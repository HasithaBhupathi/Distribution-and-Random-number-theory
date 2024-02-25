import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.zeros(N+1,dtype='float')      #### x[i] belongs to the set {0,1,....,m-1}
u = np.zeros(N,dtype='float')        #### 0<=u[i]<1
t = np.zeros(N)

a = 7**5                             #### a,c belongs to the set {0,1,....,m-1}
c = 0
m = (2**31)-1


x[0] = 1

for i in range(1,N+1):
  x[i] = (a*x[i-1]+c)%m
  u[i-1] = x[i]/m


for i in range(0,N):
  t[i] = i+1

plt.plot(t,u,'o')
plt.show()


