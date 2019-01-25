# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:25:58 2018

@author: yangyang43
"""

def is_amsteron(num):
    if type(num) != int:
        print ("Invalid input")
        return
    mystr = str(num)
    lenth = len(mystr)
    sum = 0
    for x in mystr[:]:
        sum += int(x)**lenth
        
    if sum == num:
        print ("{0} is an amsteron number".format(num))
    else:
        print ("{0} is not an amsteron number".format(num))
        
is_amsteron(408)
        