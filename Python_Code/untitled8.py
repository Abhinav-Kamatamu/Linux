# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 20:33:11 2018

@author: abhinav
"""

fibDict = {1:0,2:1}


def fib(n):
    
    try:
        return((fibDict[n]))
    except:
        fibDict[n] = (fib(n-1)+fib(n-2))        
        return(fibDict[n])


for i in range(1,1000):
    print(fib(i))

print(fibDict)
    


