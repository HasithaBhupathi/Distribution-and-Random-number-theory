import numpy as np
import matplotlib.pyplot as plt

####                  Random Amplitude Process

#### generate random numbers
N = 100
def U(x0):
   global u 
   x = np.zeros(N+1)
   u = np.zeros(N)

   x[0] = x0
   c = 10
   a = 7**5
   m = 2**31-1

   for i in range(0,N):
      x[i+1] = (a*x[i]+c)%m
      u[i] = x[i+1]/m
 
U(101)

#### Bernoulli Distribution x~Ber(p)
p = 0.5
x = []
for i in range(0,N):
    if u[i]<=p:
        x.append(1)
    else:
        x.append(0)

#### Binomial Distribution x~Bin(n,p)
n = 6
y = []
for i in range(0,60,n):
    s = 0
    for j in range(0,n):
        s = s+x[i+j]
    y.append(s)

plt.plot(y,'o')
plt.show()

#### realization of random amplitude process
O = []
for i in range(0,10):
    def f(x):
        return y[i]*np.cos(2*np.pi*1*x)

    x = np.linspace(0,10,1000)
    O.append(f(x))
    

plt.plot(x,O[0],x,O[1],x,O[2],x,O[3],x,O[4],x,O[5],x,O[6],x,O[7],x,O[8],x,O[9])
plt.show()
