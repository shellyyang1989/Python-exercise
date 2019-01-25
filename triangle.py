# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:11:27 2019
练习
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：

@author: yangyang43
"""

def triangles(n):
    mylist = [1]
    x = 0
    while (x<n+1):
        yield mylist
        x += 1
        mylist = [1] + [mylist[n] + mylist[n+1] for n in range(len(mylist)-1)] + [1]

def main():
    for i in triangles(6):
        print (i)

if __name__ == '__main__':
    main()        