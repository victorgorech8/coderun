import sys
import math
#def zet( i,r1,r2,r3):
   # z=i**3+    ((-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4)**3+   (-(-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4+r1-i)**3-r3
    #return z

n=int(input())
s1,s2,s3 = map(int,input().split())
s11=n*(n+1)/2
s21=n*(n+1)*(2*n+1)/6
s31=s11**2
r1=s11-s1
r2=s21-s2
r3=s31-s3
h=math.ceil(r3**(1/3))+1
for i in  range(1,h+1):
    if (4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2)>=0):
        y=(-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4
        z=i
        x=r1-y-z
        if (y%1==0 and x%1==0):
            if (i**3+    ((-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4)**3+   (-(-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4+r1-i)**3==r3):
                print(int(x),int(y),z)
                sys.exit()

