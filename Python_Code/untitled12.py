# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:20:21 2018

@author: abhinav
"""

n=int(input('enter a number'))
x=n
for i in range(1,n):
    v=n-i
    x=x*v
print(x)