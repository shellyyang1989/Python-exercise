# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:03:57 2019
读取文件练习，注意使用with语句，可以不写close（）
注意给filepath赋值时需要前面加r，否则特殊字符需要转义

@author: yangyang43
"""

filepath = r'D:\python\Exercise\README.md'
with open(filepath,'r') as f:
    s = f.read()
    print (s)