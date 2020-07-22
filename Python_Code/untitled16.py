# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 23:23:01 2018

@author: abhinav
"""
list=[]

for i in range(1,100):
    for j in range (1,i+1):
        list.append(i)
        
print(list[13])
print(sum(list))
print(list)
print(list[999])