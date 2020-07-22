# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:20:21 2019

@author: abhinav
"""
y=0
x=int(input('enter number:'))
an = []
def ab (x):
    y=(x*x)
    an.append(y)
    if (x!=2):
        x=x-1
        ab (x)
        
    else:
        
        an.append(1)
    return (x)
ab (x)
print (sum(an))