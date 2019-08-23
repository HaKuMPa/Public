# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:06:14 2019

@author: harshiv
"""
n=int(input())
v=int(input())
t1=int(input())
t2=int(input())
f5=int(input())
t100=int(input())

v=v/100
total=int(t1*1+t2*2+f5*5+t100*10)

if v>total:
    print("not possible")
else:
    ans=0
    for i in range(0,t1):
        for j in range(0,t2):
            for k in range(0,f5):
                for l in range(0,t100):
                    if (i+k+j+l)<=int(n) :
                        if(i*1+2*j+k*5+l*10==v):
                            ans=max(ans,i+j+k+l)
                            
    print(ans)