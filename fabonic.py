# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:11:54 2018

@author: yangyang43
"""

def fabonic(num):
    mylist = [0,1]
    lenth = len(mylist)
    while ( lenth < num):
            mylist.append(mylist[lenth-2] + mylist[lenth-1])
            lenth+=1
    print (mylist)
    
fabonic(10)
        
        
            
    