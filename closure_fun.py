# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:18:13 2019

利用闭包返回一个计数器函数，每次调用它返回递增整数：
nonlocal关键字使得闭包中内部函数可以访问和修改外部函数中定义的局部变量x，
奇妙的是当x是列表时并不需要使用该关键字, 所以有以下两种写法

@author: yangyang43
"""
'''
def createCounter():
    n = 0 
    def counter():
        nonlocal n
        n += 1
        return n
    return counter'''

def createCounter():
    n = [0]
    def counter():
        n[0] += 1
        return n[0]
    return counter
    

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('PASSED')
else:
    print('FAILED')