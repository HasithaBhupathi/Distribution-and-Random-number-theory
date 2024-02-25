import numpy as np

#### create uniforn random numbers u~U(0,1)
def uniform(N):
  global u  
  x = np.zeros(N+3)
  y = np.zeros(N+3)
  u = np.zeros(N)

  m1 = (2**32)-209
  m2 = (2**32)-22853

  x[0] = 15
  x[1] = 8
  x[2] = 25

  y[0] = 20
  y[1] = 15
  y[2] = 5

  for i in range(3,N+3):
     x[i] = (1403580*x[i-2]-810728*x[i-3])%m1
     y[i] = (527612*y[i-2]-1370589*y[i-3])%m2

  for i in range(0,N):
     if x[i+3]<=y[i+3]:
         u[i] = (x[i+3]-y[i+3]+m1)/(m1+1)
     else:
         u[i] = (x[i+3]-y[i+3])/(m1+1)


uniform(800)

####Bernoulli Distribution x~Ber(p)
p = 0.4
x = []
for i in range(0,len(u)):
    if u[i]<=p:
        x.append(1)
    else:
        x.append(0)

####Binomial Distribution x~Bin(n,p)
n = 8
y = []
for i in range(0,800,n):
    s = 0
    for j in range(0,8):
        s = s+x[i+j]
    y.append(s)

print(y)
