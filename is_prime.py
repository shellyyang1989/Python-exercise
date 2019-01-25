# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:42:29 2018

@author: yangyang43
"""

def is_primenumber(x):
    if x <= 0:
        print ("Invalid Number")
        return
    for i in range(2,x):
        print (i)
        if (x % i ==0):
            print ("{0} is not prime number".format(x))
            break
        if (x -1 == i):
            print ("{0} is prime number".format(x))
            
is_primenumber(15)
                    