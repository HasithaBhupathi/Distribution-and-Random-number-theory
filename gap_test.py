import numpy as np

N = 1000
m = (2**31)-1
a = 7**5
c = 0

x = np.zeros(N+1,dtype='float')   #### x[i] belongs to the set {0,1,....,m-1}
u = np.zeros(N,dtype='float')     #### 0<=u[i]<1
Z = []                            #### z[i] = 0,1,2,....,r,.....
T = [0]                           #### indexs of u[i] such that alpha < u[i] < beta
op =[]                            #### observed probability of each class
ep = []                           #### expected probability

x[0] = 100

for i in range(0,N):
   x[i+1] = (a*x[i]+c)%m
   u[i] = x[i+1]/m


alpha = 0.4
beta = 0.6
r = 7                             #### The integer r should be chosen so that the expected number per class is > 5.
p = beta-alpha

#### find the random number wich in between (alpha,beata)
for i in range(0,N):
    if alpha < u[i] < beta:
        T.append(i+1)

                                  #### expected number of random numbers in (alpha,beta)  given by  N*(beata-alpha) ~ len(T)-1           

#### create the gap vector
for i in range(0,len(T)-1):
    Z.append(T[i+1]-T[i]-1) 

#### find observation and expected probability of each class
for i in range(min(Z),r):
       op.append(Z.count(i)/len(Z))       #### observation
       ep.append(p*((1-p)**i))            #### expected 

add = 0       
for i in range(r,max(Z)+1):
       add = add+Z.count(i)
       
op.append(add/len(Z))
ep.append((1-p)**r)

print(u)
print(T)
print(Z)
print(op)
print(ep)

#### find test statistic
x_cal = 0
for i in range(0,len(ep)):
   x_cal = x_cal + ((ep[i]-op[i])**2)/ep[i]


k = 8
alpha = 0.05                    #### probability of type 1 error
lower_tail = 1.69               #### gratest lower bound of confident interval
upper_tail = 16.013             #### least upper bound of confident interval

#### rejection rule
if lower_tail<=x_cal<=upper_tail:
   print("There is no evidence to reject the null hypothesis")
else:
   print("We reject the null hypothesis")   


