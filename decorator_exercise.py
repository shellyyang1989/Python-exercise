# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:32:48 2019

1. 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
2. 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志

@author: yangyang43
"""
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        f = fn(*args, **kwargs)
        end = (time.time()-start)
        print('%s executed in %s ms' % (fn.__name__, end))
        return f
    return wrapper

def log(text=None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print("begin call")
            if text != None:
                print ("%s %s" % (text, fn.__name__))
            f = fn(*args, **kwargs)
            print("end call")
            return f
        return wrapper
    return decorator
            

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
    
@log()
def test():
    pass

@log('execute')
def test1():
    pass

t = test()
t1 = test1()