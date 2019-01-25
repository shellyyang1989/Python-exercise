# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:12:12 2018

@author: yangyang43
"""

def reverse_list(L):
    lenth = len(L)
    i = 0
    while (i < lenth/2):
        L[lenth-1-i],L[i] = L[i],L[lenth-1-i]
        i += 1
    
myList = [1,2,3,4,5,6]    
reverse_list(myList)
print (myList)