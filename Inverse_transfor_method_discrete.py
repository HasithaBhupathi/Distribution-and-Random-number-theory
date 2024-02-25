import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.zeros(N+1,dtype='float')                       #### x[i] belongs to the set {0,1,2,.....m-1}
u = np.zeros(N,dtype='float')                         #### 0<=u[i]<1
r = np.array([1,2,3,4,5])                             #### state space
p = np.array([0.2,0.3,0.1,0.05,0.35],dtype='float')   #### probability of each state
F = [0]                                               #### cumulative function
inverse = np.zeros(N)                                 #### contain inverse of F  

a = 7**5
c = 0
m = (2**31)-1
x[0] = 1

#### create random numbers
for i in range(0,N):
   x[i+1] = (a*x[i]+c)%m
   u[i] = x[i+1]/m

#### cumulative function
for i in range(0,len(p)):
    F.append(F[i]+p[i])

#### create inverse of each u    
for i in range(0,N):
    for j in range(0,len(F)-1):
       if F[j]<u[i]<=F[j+1]:
           inverse[i] = r[j]

print(F)
print(u)
print(inverse)

bins = [0.5,1.5,2.5,3.5,4.5,5.5]
plt.hist(inverse,bins,ec='r')
plt.title("Inverse transform method")
plt.ylabel("frequence")
plt.xlabel("values of random variables")
plt.show()
                      

  
