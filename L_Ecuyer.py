#### L'Ecuyer method is a combination of MRG

import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.zeros(N+3,dtype = 'float')   ### x[i] belongs to the set {0,1,....mx-1}
y = np.zeros(N+3,dtype = 'float')   ### y[i] belongs to the set {0,1,....my-1}
u = np.zeros(N,dtype = 'float')     ### 0<= u[i] < 1
t = np.zeros(N)

x[0] = 12564
x[1] =7856
x[2] = 785496

y[0] = 10
y[1] = 4586
y[2] = 785496
   
mx = (2**32)-209
my = (2**32)-22853

for i in range(3,N+3):
   x[i] = (1403580*x[i-2]-810728*x[i-3])%mx
   y[i] = (527612*y[i-2]-1370589*y[i-3])%my

for i in range(0,N):
   if x[3+i]<=y[3+i]:
      u[i] = (x[3+i]-y[3+i]+mx)/(mx+1)
   else:
      u[i] = (x[3+i]-y[3+i])/(mx+1)   


for i in range(0,N):
  t[i] = i+1

plt.plot(t,u,'o')
plt.title("Scatterplot")
plt.show()
