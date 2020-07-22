# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:35:17 2018

@author: abhinav
"""

numberOfLines =int(input('enter the number of lines:'))

for i in range(1,numberOfLines+1):
    print((numberOfLines-i)*" "+(2*i-1)*"*")
for j in range(1,numberOfLines):
    print((j)*' '+(2*(numberOfLines-j)-1)*"*")
    