# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:21:23 2018

@author: yangyang43
"""

def is_leapyear(year):
    if (year % 4) == 0 and (year % 100) !=0:
        print ("{0} is leap year".format(year))
    elif (year % 400) == 0:
        print ("{0} is leap year".format(year))
    else:
        print ("{0} is not leap year".format(year))
        
is_leapyear(2001)
    
        