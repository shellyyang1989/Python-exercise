# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 10:58:14 2019

回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
写函数判断一个数是否是回数

@author: yangyang43
"""
def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def main():
    num = input("Please input a iteger\n")
    print (is_palindrome(num))
    
if __name__ == '__main__':
    main()    
