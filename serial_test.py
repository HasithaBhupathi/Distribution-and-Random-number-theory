import numpy as np
import matplotlib.pyplot as plt

#### genarate uniform random numbers
N = 1000
m = 2**31-1
a = 117
c = 1

x = np.zeros(N+1,dtype='float')
u = np.zeros(N,dtype='float')

x[0] = 1

for i in range(0,N):
   x[i+1] = (a*x[i]+c)%m
   u[i] = x[i+1]/m

r1 = []
r2 = []

for i in range(0,N,2):
   r1.append(u[i])
   
for i in range(1,N,2):
   r2.append(u[i])

#### plot graph
plt.plot(r1,r2,'.')
plt.xticks(np.arange(0,1.1,0.1))
plt.yticks(np.arange(0,1.1,0.1))
plt.title("Serial test")
plt.xlabel('r1')
plt.ylabel('r2')
plt.xlim([0,1])
plt.ylim([0,1])
plt.grid()
plt.show()

#### count points (observation frequency)
k = 10
z = np.zeros((k,k))

for i in range(0,int(N/2)):
   for j in range(0,k):
      for m in range(0,k):
         if (1/k)*j<=r1[i]<=(1/k)*(j+1) and (1/k)*m<=r2[i]<=(1/k)*(m+1):
            z[m,j]=z[m,j]+1

#### find expected values
exp = N/(2*(k**2))

#### sumation of frequency deferences of each cell (test statistic = x_cal)
x_cal = 0
for i in range(0,k):
   for j in range(0,k):
      x_cal = x_cal+((z[i,j]-exp)**2)/exp

#### degree of freedom
dof = k**2-1

aplha = 0.05  #### significant level
lower_tail =  73.361
upper_tail =  128.422

#### H0:random number generator is indeed uniformly distributed
#### H1:random number generator is not indeed uniformly distributed

if lower_tail<=x_cal<=upper_tail:
   print("There is no evidence to reject the null hypothesis")
else:
   print("We reject the null hypothesis")   

      







