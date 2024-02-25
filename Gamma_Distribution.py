import numpy as np
import matplotlib.pyplot as plt


#### generate random numbers u~U(0,1) and Z~N(0,1)
N = 12000
M = 1000
x = np.zeros(N+1)
y = np.zeros(N+1)
z = np.zeros(N+1)

u = np.zeros(N)
v = np.zeros(N)
w = np.zeros(N)
s = np.zeros(N)

a = 117
b = 113
c = 211

x[0] = 10
y[0] = 1
z[0] = 15

m1 = 2**31-1
m2 = 2**11-1
m3 = 2**17-1

for i in range(0,N):
    x[i+1] = (a*x[i])%m1
    y[i+1] = (b*y[i])%m2
    z[i+1] = (c*z[i])%m3

    u[i] = x[i+1]/m1
    v[i] = y[i+1]/m2
    w[i] = z[i+1]/m3

    s[i] = ((-2*np.log(v[i]))**0.5)*np.sin(2*np.pi*w[i])

#### pdf f(x;a,l) = (l**a)*(x**(a-1))*(e**(-l*x))/L(a) L is the gamma function x>=0
#### X~Gamma(a,l)
#### X/lamda~Gamma(alpha,lamda)

def gamma(alpha):
    global op
    op = []
    #### Gamma(alpha,1) generator for alpha>=1
    if alpha>=1:
        r = np.zeros(N)
        d = alpha-(1/3)
        c = 1/((9*d)**0.5)
        
        for i in range(0,N):
            r[i] = (1+c*s[i])**3
            if (s[i]>-(1/c)) and np.log(u[i])<(0.5*s[i]**2+d-d*r[i]+d*np.log(r[i])) and len(op)<M:
                op.append(d*r[i])
        
        plt.hist(op,ec = 'white')
        plt.show()

    #### Gamma(alpha,1) generate for alpha<1
    else:
        d = 0.07+0.75*(1-alpha)**0.5
        b = 1+np.exp(-d)*(alpha/d)

        u1 = u
        u2 = w
        v = b*u1
        op = []
    
        for i in range(0,N):
            if v[i]<=1 and len(op)<M:
                X = d*v[i]**(1/alpha)
                if u2[i]<=(2-X)/(2+X):
                    op.append(X)
                else:
                    if u2[i]<=np.exp(-X):
                        op.append(X)
                          
            elif v[i]>1 and len(op)<M:
                X = -np.log(d*(b-v[i])/alpha)
                Y = X/d
                if u2[i]*(alpha+Y*(1-alpha))<=1:
                    op.append(X)
                else:
                    if u2[i]<Y**(alpha-1):
                        op.append(X)
                        
        plt.hist(op,ec='white')
        plt.show()

        

gamma(2.5)
print(op)

    
