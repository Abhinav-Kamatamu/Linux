# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:13:33 2018

@author: abhinav
"""
import string


input_string=(input('Please enter a string : '))
out_string = ""
orig_string = ''
for i in input_string:
    out_string = out_string + "%03d"%ord(i)

print(out_string)

