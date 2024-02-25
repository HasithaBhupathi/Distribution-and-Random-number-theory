import numpy as np
import matplotlib.pyplot as plt

####                  Random walk

#### generate uniform randomnumbers

N = 100
def U(x0):
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

 
def q4(u1,u2):
   #### genarate standard normal distribution random numbers
   z = []
   for i in range(0,N):
      z.append(((-2*np.log(u1[i]))**0.5)*np.sin(2*np.pi*u2[i]))

   #### random walk   
   x = [0]
   for i in range(0,N):
      x.append(sum(z[0:i+1]))
   
   return x  

t = []
for i in range(0,N+1):
    t.append(i)
    
plt.plot(t,q4(U(101),U(51)))
plt.show()

v = [51,101,207,311,407,511]
walk = []

for i in range(0,len(v)-1):
    walk.append(q4(U(v[i]),U(v[i+1])))
    
plt.plot(t,walk[0],t,walk[1],t,walk[2],t,walk[3],t,walk[4])
plt.show()
