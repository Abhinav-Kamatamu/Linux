# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:21:26 2018

@author: abhinav
"""

def de(n):
    out_string=(input('enter code'))
    orig_string=''
    while out_string != "":
        orig_string = orig_string + ( chr(int(out_string[:3])))
        out_string= out_string[3:]   
    
    return(orig_string)