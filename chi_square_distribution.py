import numpy as np
import matplotlib.pyplot as plt

N = 1000
m = 2**12
a = 125
c = 1

x = np.zeros(N+1)                #### x[i] belongs to the set {0,1,2,....,m-1}
u = np.zeros(N,dtype='float')    #### 0<=u[i]<1
t = np.zeros(N)

x[0] = 1

for i in range(1,N+1):
   x[i] = (a*x[i-1]+c)%m
   u[i-1] = x[i]/m
   t[i-1] = i

#### H0:random number generator is indeed uniformly distributed
#### H1:random number generator is not indeed uniformly distributed

alpha = 0.05                    #### probability of type 1 error
lower_tail = 2.70               #### gratest lower bound of confident interval X**2(1-alpha/2,k-1)
upper_tail = 19.023             #### least upper bound of confident interval   x**2(alpha/2,k-1)
exptd = 100                     #### expected frequence of each bin
k = 10                          #### number of bins
o = np.zeros(k)                 #### observation frequence of each bin
D = np.zeros(k,dtype='float')   ##### ((oi-ei)**2)/ei value for each bin
bin_range = np.zeros(k+1,dtype='float')  #### boundry points of bins

for i in range(0,k):
   bin_range[i+1] = bin_range[i]+0.1
   
#### find observation frequence of each bin
for i in range(0,k):
  n = 0
  for j in range(0,N):
      if bin_range[i]<=u[j]<bin_range[i+1]:
          n = n+1      
  o[i] = n

#### find ((oi-ei)**2)/ei value of each bin
for i in range(0,k):
   D[i] = ((o[i]-exptd)**2)/exptd

x_cal = sum(D)               #### test static

if lower_tail<=x_cal<=upper_tail:
   print("There is no evidence to reject the null hypothesis")
else:
   print("We reject the null hypothesis")   

plt.hist(u,10,ec='red')
plt.title("Histogram")
plt.show()

