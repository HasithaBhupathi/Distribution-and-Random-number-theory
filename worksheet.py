import numpy as np
import matplotlib.pyplot as plt

#### Question 1
def U(x0):
    
   N = 100
   x = np.zeros(N+1)
   global u
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

plt.hist(u,ec='white')
plt.show()

plt.plot(u,'o')
plt.show()

#### Question 2(Random Amplitude Process)
#### part 1

####Bernoulli Distribution x~Ber(p)
p = 0.5
x = []
for i in range(0,len(u)):
    if u[i]<=p:
        x.append(1)
    else:
        x.append(0)

####Binomial Distribution x~Bin(n,p)
n = 6
y = []
for i in range(0,60,n):
    s = 0
    for j in range(0,n):
        s = s+x[i+j]
    y.append(s)

plt.plot(y,'o')
plt.show()

#### part 2
O = []

for i in range(0,10):
    def f(x):
        return y[i]*np.cos(2*np.pi*1*x)

    x = np.linspace(0,10,100)
    O.append(f(x))

plt.plot(x,O[0],x,O[1],x,O[2],x,O[3],x,O[4],x,O[5],x,O[6],x,O[7],x,O[8],x,O[9])
plt.show()

#### Question 3(Simple Random Walk (Drunkard’s Walk))

####Bernoulli Distribution x~Ber(p)
def q3(u):
   #### part 1 
   p = 0.5
   z = []
   x = []
   for i in range(0,100):
      if u[i]<=p:
         z.append(1)
      else:
         z.append(-1)

   #### part 2
   for i in range(0,100):
     x.append(sum(z[0:i]))

   return z,x

plt.hist(q3(u)[0],ec='white')
plt.show()

t = np.linspace(0,1,100)
plt.plot(t,q3(u)[1])
plt.show()

#### part 3
v = [51,101,207,311,407]
walk = []
for i in range(0,len(v)):
    walk.append(q3(U(v[i]))[1])
    
plt.plot(t,walk[0],t,walk[1],t,walk[2],t,walk[3],t,walk[4])
plt.show()

#### Question 4( Random walk)
def q4(u1,u2):
   #### part 1
   z = []
   for i in range(0,100):
      z.append(((-2*np.log(u1[i]))**0.5)*np.sin(2*np.pi*u2[i]))

   #### part 2
   x = []
   for i in range(0,100):
      x.append(sum(z[0:i]))

   return x,z   

plt.hist(q4(U(101),U(51))[1],ec='white')
plt.show()

plt.plot(t,q4(U(101),U(51))[0])
plt.show()

#### part 3
v = [51,101,207,311,407,511]
walk = []
for i in range(0,len(v)-1):
    walk.append(q4(U(v[i]),U(v[i+1]))[0])
    
plt.plot(t,walk[0],t,walk[1],t,walk[2],t,walk[3],t,walk[4])
plt.show()


#### Question 5(poisson process)
y = []
x = []
lam = 0.8
U(101)

for i in range(0,len(U(101))):
   y.append(-np.log(u[i])/lam)
   x.append(sum(y[0:i]))

t = np.linspace(0,25,100)
plt.step(t,x)
plt.show()


#### Question 6(wiener process)
N = 101

x = np.zeros(N+1)
y = np.zeros(N+1)
u1 = np.zeros(N)
u2 = np.zeros(N)

z = np.zeros(N)   #### for standard normal distribution

x[0] = 100
y[0] = 10
m1 = (2**32)-1
m2 = (2**32)-1157

for i in range(0,N):
  x[i+1] = (170*x[i])%m1
  y[i+1] = (172*y[i])%m2

  u1[i] = x[i+1]/m1
  u2[i] = y[i+1]/m2
  
#### standard Normal distributions by box-muller approach ( peack occure near mean = 0)
  z[i] = ((-2*np.log(u1[i]))**0.5)*np.sin(2*np.pi*u2[i])  #### we can use both sin or cosin

t = np.zeros(N)
for i in range(1,N):
    t[i] = t[0]+0.01*i

w = np.zeros(N)
for i in range(1,N):
    s = 0
    for j in range(1,i+1):
        s = s+z[j]
    w[i] = (t[i]-t[i-1])**0.5*s

plt.plot(t,w)
plt.show()

#### Question 07 (Brownian motion)
d = 5
dc = 9
b = np.zeros(N)

for i in range(0,N):
   b[i] = d*t[i]+dc*w[i]

plt.plot(t,b,t,w)
plt.show()

