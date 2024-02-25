import numpy as np
import matplotlib.pyplot as plt

#### pdf f(x) = (b/pi)*(1/((x-a)**2+b**2)))
#### PMF F(x) = integrate(-infinity to x) of f(t)
#### standard cauchy when b = 1 and a = 0

#### Standard Cauchy(0,1) generator via ratio of normals
N = 100000

x = np.zeros(N+1)
y = np.zeros(N+1)
z = np.zeros(N+1)
p = np.zeros(N+1)

u = np.zeros(N)
r = np.zeros(N)
s = np.zeros(N)
t = np.zeros(N)

x[0]=10
y[0]=12
z[0]=15
p[0]=18

a = 117
b = 213
c = 111
d = 313

m1 = (2**31)-1
m2 = (2**21)-1
m3 = (2**11)-1
m4 = (2*17)-1

A = np.zeros(N)
B = np.zeros(N)
C = np.zeros(N)

for i in range(0,N):
    x[i+1] = (a*x[i])%m1
    y[i+1] = (a*y[i])%m2
    z[i+1] = (a*z[i])%m3
    p[i+1] = (a*p[i])%m4
    
    u[i] = x[i+1]/m1
    r[i] = y[i+1]/m2
    s[i] = z[i+1]/m3
    t[i] = p[i+1]/m4
    
    A[i] = ((-2*np.log(u[i]))**0.5)*np.sin(2*np.pi*r[i])
    B[i] = ((-2*np.log(s[i]))**0.5)*np.sin(2*np.pi*t[i])
    C[i] = A[i]/B[i]

plt.hist(C,bins=100)
plt.show()


#### Standard cauchy generator(This algorithem does not work)
"""
for i in range(0,N):
    u[i] = np.tan(np.pi*(u[i]-1/2))

plt.plot(u)
plt.show()
"""

#### using standard cauchy(0,1) random number genarator
s = np.random.standard_cauchy(100000)
s = s[(s>-25)&(s<25)]

plt.hist(s,bins=100)
plt.show()
