#### Whichman hill is a combination of LCG

import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.zeros(N+1,dtype='float')   #### x[i] belongs to the set {0,1,...,m1-1}
y = np.zeros(N+1,dtype='float')   #### y[i] belongs to the set {0,1,....m2-1}
z = np.zeros(N+1,dtype='float')   #### z[i] belongs to the set {0,1,....m3-1}
u = np.zeros(N,dtype='float')     #### 0<= u[i] < 1 
t = np.zeros(N)

m = np.array([[30269],[30307],[30323]])

x[0] = 1
y[0] = 15867
z[0] = 24856

for i in range(1,N+1):
   x[i] = (171*x[i-1])%m[0]
   y[i] = (172*y[i-1])%m[1]
   z[i] = (170*z[i-1])%m[2]
 
   u[i-1] = (x[i]/m[0]+y[i]/m[1]+z[i]/m[2])%1  

for i in range(0,N):
  t[i] = i+1


plt.plot(t,u,'o')
plt.title("Scatterplot")
plt.show()

