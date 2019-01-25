# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:56:55 2018

@author: yangyang43
"""

def is_number(x):
    try:
        print (x.isdigit())
    except:
        pass
    try:
        print (x.isnumeric())
    except:
        pass

is_number('12345')
