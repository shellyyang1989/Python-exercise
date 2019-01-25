# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:19:31 2018

@author: yangyang43
"""

def bubble_sort(lists):
    lists_len = len(lists)
    for i in range(lists_len):
        for j in range(lists_len-i-1):
            if lists[j] > lists[j+1]:
                lists[j],lists[j+1] = lists[j+1],lists[j]
myList = [10,2,9,3,4,1]                
bubble_sort(myList)
print(myList)
    