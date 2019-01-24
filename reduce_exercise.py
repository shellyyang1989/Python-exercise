# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 22:20:23 2019

Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：

@author: yangyang43
"""
from functools import reduce

def main():
    mylist = [1,2,3,4,5]
    result = reduce((lambda x,y:x*y), mylist)
    print (result)
if __name__ == '__main__':
    main()    