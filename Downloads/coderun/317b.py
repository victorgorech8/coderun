import sys
import math
n=int(input())
s1,s2,s3 = map(int,input().split())
s11=n*(n+1)/2
s21=n*(n+1)*(2*n+1)/6
s31=s11**2
r1=s11-s1
r2=s21-s2
r3=s31-s3
h=math.ceil(r3**(1/3))-1
for i in range (1,h-1):
    if(   (i**3+    ((-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4)**3+   (-(-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4+r1-i)**3  )==r3 ):
        z=i
        break

y=int((-2*(-r1+z)+(4*(-r1+z)**2-8*(r1**2-r2-2*r1*z+2*z**2))**(1/2))/4)
x=int(r1-z-y)
print(x,y,z)
