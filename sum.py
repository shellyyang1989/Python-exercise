# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:54:31 2018

@author: yangyang43
"""

def sum(L):
    x = 0 
    for i in L[1::2]:
        x += i
    print (x)
        
myList = [1,2,3,4,5,6]
sum(myList)
