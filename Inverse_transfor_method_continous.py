import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.zeros(N+1,dtype='float')
u = np.zeros(N,dtype='float')
t = np.zeros(N)

a = 7**5
m = (2**31)-1
c = 0
x[0] = 100

"""
for i in range(1,N+1):
   x[i] = (a*x[i-1]+c)%m
   u[i-1] = (x[i]/m)**0.5  #### x = U**0.5 when f(x) = 2x ;0<=x<=1
   t[i-1] = i   
"""

for i in range(1,N+1):
   x[i] = (a*x[i-1]+c)%m
   u[i-1] = np.log(1/(1-(x[i]/m))**0.5)  #### x = ln(1/((1-U)**0.5)) when f(x) = 1-(e**-2x) ;0<x
   t[i-1] = i   


plt.plot(t,u,'o')
plt.title("Scatterplot")
plt.show()
