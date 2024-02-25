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


uniform(100)

####Uniform discrete Distribution x ~Du(a,b)
a = 5
b = 15
x = []
for i in range(0,len(u)):
    x.append(np.floor(a+(b-a+1)*u[i]))

print(x)    

