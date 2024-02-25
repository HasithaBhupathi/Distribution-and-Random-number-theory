import numpy as np
import matplotlib.pyplot as plt

#### inputs
N = 1000
m = 2**12
a = 125
c = 1

#### create list
x = np.zeros(N+1,dtype='float')    #### x[i] belongs to the set {0,1,2,...,m-1}
u = np.zeros(N,dtype='float')      #### 0<=u[i]<1
D1 = np.zeros(N,dtype='float')     #### D1[i] = (i/N)-u[i]
D2 = np.zeros(N,dtype='float')     #### D2[i] = u[i]-(i-1)/N  
 
x[0] = 1

#### generate random numbers
for i in range(0,N):
   x[i+1] = (a*x[i]+c)%m
   u[i] = x[i+1]/m    


   
#### change u in asending order
u.sort()

#### create D1 and D2 list
for i in range(0,N):
    D1[i] = ((i+1)/N)-u[i]   #### D+
    D2[i] = u[i]-((i)/N)     #### D-

#### defined max(D1,D2)
D_cal = max(max(D1),max(D2))

alpha = 0.05
dic = {0.2:1.07,0.15:1.14,0.1:1.22,0.05:1.36,0.01:1.63}

#### calculate the crirical value
if N>35 and (alpha in dic.keys()):     
     D_table = dic.get(alpha)/(N**0.5)
else:
     D_table = 0.565       ####  for N = 5 and alpha = 0.10
           
#### rejection criteria
if D_cal>D_table:
   print("We reject the null hypothesis")
else:
   print("There is no evidence to reject the null hypothesis")

plt.hist(u,10,ec='black')
plt.title("Histogram")
plt.show()
 
