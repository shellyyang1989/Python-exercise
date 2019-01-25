# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:39:48 2018

@author: yangyang43
"""

def bubble(myList):
    lenth = len(myList)
    for i in range(lenth):
        for j in range(lenth-i-1):
            if myList[j] > myList[j+1]:
                myList[j],myList[j+1] = myList[j+1],myList[j]
    print (myList)
    
testList = [5,1,9,3,2]
bubble(testList)