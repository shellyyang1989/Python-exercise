# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 22:37:19 2019

用filter求素数

计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

除了2以外，所有的偶数都不是素数，所以以下算法只对奇数运算即可

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。

@author: yangyang43
"""

def gennum():
    n = 1
    while True:
        n += 2
        yield n
        
def not_visi(n):
    return lambda x:x%n >0

def primes():
    yield 2
    it = gennum()
    while True:
        n = next(it)
        yield n
        it = filter(not_visi(n), it)
        
def main():
    for i in primes():
        if i < 1000:
            print (i)
        else:
            break

if __name__ == '__main__':
    main()        

        