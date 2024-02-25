import numpy as np
import matplotlib.pyplot as plt

####                     Simple Random Walk (Drunkard’s Walk)

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

   return u

U(101)

def q3(u):
   ####Bernoulli Distribution x~Ber(p)
   p = 0.5
   z = []
   for i in range(0,N):
      if u[i]<=p:
         z.append(1)
      else:
         z.append(-1)

   #### generate a random walk
   global x
   x = [0]
   for i in range(0,N):
     x.append(sum(z[0:i+1]))
   
   return x  
     
q3(u)

t = []
for i in range(0,N+1):
   t.append(i)
   
plt.plot(t,x)
plt.show()   

#### genarate many random walks
v = [51,101,207,311,407]
walk = []

for i in range(0,len(v)):
    walk.append(q3(U(v[i])))
    
plt.plot(t,walk[0],t,walk[1],t,walk[2],t,walk[3],t,walk[4])
plt.show()

