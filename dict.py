# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:32:54 2018

@author: yangyang43
"""

astr="k:1|k1:2|k2:3|k3:4"
alist = astr.split('|')
adict ={}
for i in alist:
    key,value=i.split(':')
    adict[key]= value
print(adict)