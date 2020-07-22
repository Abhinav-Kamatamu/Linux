# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 23:23:01 2018

@author: abhinav
"""

def is_good(n):
    for i in range(1,n):
        sm = 0
        for j in range(i,n):
            sm = sm + j
            if (sm == n):
                return (False)
            if (sm > n):
                break
    return(True)


for i in range(1,10000):
    if is_good(i):
        print (i) 