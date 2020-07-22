# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:37:40 2018

@author: abhinav
"""

#=int(input("type the number you want to find if it is a perfect number or not :" ))
for n in range(1,30):
    sum=0
    for i in range(1,n):
            if(n%i==0):
                sum=sum+i
    if (sum==n):
        print (n," is a perfect number")
                
    else:
        print (n," is not a perfect number")        
        
    