import numpy as np
import matplotlib.pyplot as plt
import math

#### Acceptance and rejection method
#### U ~U(0,1)        
N = 10**4

x = np.zeros(N+1)
y = np.zeros(N+1)
z = np.zeros(N+1)
u = np.zeros(N)

x[0] = 100
y[0] = 200
z[0]=  500

m1 = 30269
m2 = 30307
m3 = 30323

for i in range(0,N):
    x[i+1] = (171*x[i])%m1
    y[i+1] = (172*y[i])%m2
    z[i+1] = (170*z[i])%m3
    u[i] = (x[i+1]/m1+y[i+1]/m2+z[i+1]/m3)%1
 
#### V ~v(0,1)
x = np.zeros(N+1)
v = np.zeros(N)
x[0] = 100
m1 = 30269

for i in range(0,N):
   x[i+1] = (171*x[i])%m1
   v[i] = x[i]/m1

#### f(x) = sin(x)/2 0<=x<=pi
#### g(x) = x 0<=x<=pi
#### c = 1
#### cg(x)>=f(x) for all x in [0,pi]

#### cumulative function of g is G(x) = (x**2)/2
y = []
i = 0

while len(y)<1000:
   r = (2*u[i]*(math.pi**2)/2)**0.5
   if (v[i]<=(math.sin(r)/2)/(1*r)):
       y.append(r)        
   i = i+1

plt.hist(y,ec='r')
plt.title('Acceptance and rejection method of question 5')
plt.xlabel("values of random variable")
plt.ylabel("frequency")
plt.show()
