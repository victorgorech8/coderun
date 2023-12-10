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
h=math.ceil(r3**1/3)-1
for i in range (1,h-1):
    for j in range (i+1,h):
        for k in range (j+1,h+1):
            if (i+j+k==r1)and (i**2+j**2+k**2==r2)and(i**3+j**3+k**3==r3):
                print(i,j,k)
                sys.exit()
