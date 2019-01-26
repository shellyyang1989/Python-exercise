# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:32:48 2019

请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

@author: yangyang43
"""
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrap(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn
    return wrap

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('FAILED')
elif s != 7986:
    print('PASSED')
    
