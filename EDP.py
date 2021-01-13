import numpy as np
import matplotlib.pyplot as plt


nbrItr=300

L1=120;
L2=80;
L3=50; 
L4=15;
h=1;

tempInt=250;
tempExt=40;

m=round(L1/h)
n=round(L2/h)
m1=round((L1-L3)/(2*h))
n1=round((L2-L4)/(2*h))
m2=m1+round(L3/h)
n2=n1+round(L4/h)

T = np.zeros([n,m],dtype=float)
for i in range(0,n):
    for j in range(0,m):
        T[i,j]=tempInt
        
for i in range(0,n):
     T[i,0]=tempExt
     T[i,m-1]=tempExt
     
for j in range(0,m):
     T[0,j]=tempExt
     T[n-1,j]=tempExt
     
 
     
for k in range(0,nbrItr):
    for i in range(1,n-1):
        for j in range(1,m1):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
            
    for i in range(1,n-1):
        for j in range(m2,m-1):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
            
    for i in range(1,n1-1):
        for j in range(m1,m2):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])

    for i in range(n2+1,n-1):
        for j in range(m1,m2):
            T[i,j]=0.25*(T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])
 
 


plt.imshow(T)
plt.show()

x=range(0,m)
y=range(0,n)

plt.contour(x,y,T)
plt.colorbar()
plt.show()