# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:12:26 2018

@author: yangyang43
"""

def append_List(L1,L2):
    for i in L2:
        L1.append(i)
    print (L1)

myList1 = [1,2,3]
myList2 = ['a','b','c']
append_List(myList1,myList2)