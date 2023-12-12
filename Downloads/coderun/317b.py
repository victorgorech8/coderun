import sys
import math
def zet( i,r1,r2,r3):
    z=i**3+    ((-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4)**3+   (-(-2*(-r1+i)+(4*(-r1+i)**2-8*(r1**2-r2-2*r1*i+2*i**2))**(1/2))/4+r1-i)**3-r3
    return z

n=int(input())
s1,s2,s3 = map(int,input().split())
s11=n*(n+1)/2
s21=n*(n+1)*(2*n+1)/6
s31=s11**2
r1=s11-s1
r2=s21-s2
r3=s31-s3
h=math.ceil(r3**(1/3))+1
i=math.floor(h/2)
if (zet(n,r1,r2,r3)==0):
    z=n
    y=int((-2*(-r1+z)+(4*(-r1+z)**2-8*(r1**2-r2-2*r1*z+2*z**2))**(1/2))/4)
    x=int(r1-z-y)
    print(x,y,z)
    sys.exit()

if (zet(1,r1,r2,r3)==0):
    z=1
    y=int((-2*(-r1+z)+(4*(-r1+z)**2-8*(r1**2-r2-2*r1*z+2*z**2))**(1/2))/4)
    x=int(r1-z-y)
    print(x,y,z)  
    sys.exit()
a=1
b=h   
while(abs(a-b)>1):
    if (zet(i,r1,r2,r3)==0):
        z=i
        y=int((-2*(-r1+z)+(4*(-r1+z)**2-8*(r1**2-r2-2*r1*z+2*z**2))**(1/2))/4)
        x=int(r1-z-y)
        print(x,y,z)
        sys.exit()

    if (zet(i,r1,r2,r3)<0):
        a=i
    if(zet(i,r1,r2,r3)>0):
        b=i
    i=a+math.floor(b-a)


if (zet(a,r1,r2,r3)==0):
    z=a
    y=int((-2*(-r1+z)+(4*(-r1+z)**2-8*(r1**2-r2-2*r1*z+2*z**2))**(1/2))/4)
    x=int(r1-z-y)
    print(x,y,z)
    sys.exit()

if (zet(b,r1,r2,r3)==0):
    z=b
    y=int((-2*(-r1+z)+(4*(-r1+z)**2-8*(r1**2-r2-2*r1*z+2*z**2))**(1/2))/4)
    x=int(r1-z-y)
    print(x,y,z)  
    sys.exit()    

