# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:25:58 2018

@author: yangyang43
"""

alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
alist.sort(key=lambda x:x['age'])
print(alist)