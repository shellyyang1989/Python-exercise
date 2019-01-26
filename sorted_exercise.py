# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:26:01 2019
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
注意，key= 接收自定义函数，调用时在key里可以不加参数，sorted默认把
列表里所有元素作为key函数的参数，所以只需定义函数

@author: yangyang43
"""

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]
    
def main():
    l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    l2 = sorted(l, key=by_name)
    l3 = sorted(l, key=by_score)
    print (l2, l3)
    
if __name__ == '__main__':
    main()    
    
    