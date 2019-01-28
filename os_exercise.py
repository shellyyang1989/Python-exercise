# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:08:10 2019

1. 利用os模块编写一个能实现dir -l输出的程序。

2. 编写一个程序，能在当前目录以及当前目录的所有子目录下
查找文件名包含指定字符串的文件，并打印出相对路径。

@author: yangyang43
"""

import os
def ldir():
    return os.listdir('.')
    
def ffile(str):
    l = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if str in file:
                l.append(file)
        for dir in dirs:
            for root1, dirs1, files1 in os.walk(dir):
                for file1 in files1:
                    if str in file:
                        filepath = os.path.join(dir, file)
                        l.append(filepath)
    return l    
                    
print (ldir())
print (ffile("exercise"))                        
                        
    
    