import math
import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.zeros(N+1,dtype='float')      #### x[i] belongs to the set {0,1,....,m-1}
u = np.zeros(N,dtype='float')        #### 0<=u[i]<1

a = 7**5                             #### a,c belongs to the set {0,1,....,m-1}
c = 0
m = (2**31)-1

x[0] = 1

for i in range(1,N+1):
  x[i] = (a*x[i-1]+c)%m
  u[i-1] = x[i]/m

U = u                          #### random numbers U~U(0,1)
NU = []                        #### maltipy random numbers from sum(xi)
C_NU = []                      #### ceiling of n*u values
X = [1,2,3]                    #### domain values of function 
Y = []                         #### output values
T = []                         #### table lookup values
n = 6                          #### sum(x1)

for i in range(0,len(U)):
    NU.append(U[i]*n)
    C_NU.append(math.ceil(NU[i]))
    
for i in range(0,len(X)):
    for j in range(0,X[i]):
        T.append(X[i])

for i in range(0,len(C_NU)):
    Y.append(T[C_NU[i]-1])

bins = [0.5,1.5,2.5,3.5]
plt.hist(Y,bins,ec='r')
plt.show()
