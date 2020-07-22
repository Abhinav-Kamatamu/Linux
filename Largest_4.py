# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:42:18 2016

@author: abhinav
"""

a = 12300
b = 900
c = 567
d = 124

if (a > b):
    if (a > c):
        if (a > d):
            print (a)
        else:
            print (d)    
    else:
        if (c > d):
            print (c)
        else:
            print (d)
else:
    if (b > c):
        if (b > d):
            print (b)
        else:
            print (d)
    else:
        if (c > d):
            print (c)
        else:
            print (d)