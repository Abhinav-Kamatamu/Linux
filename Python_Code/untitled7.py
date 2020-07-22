# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 19:36:01 2018

@author: abhinav
"""

prenum=1
preprenum=0
def fib (n):
    if (n==1):
        return(0)
    if (n==2):
        return(1)
    return (fib(n-1)+fib(n-2))

for i in range(1,100):
    print(i, " ->",fib(i))    