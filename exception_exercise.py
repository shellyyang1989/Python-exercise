# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:17:35 2019
异常处理练习, buildin exception架构如下
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

@author: yangyang43
"""

from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
        
    