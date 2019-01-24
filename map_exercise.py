# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:33:48 2019

利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']

@author: yangyang43
"""
    
def main():
    mylist = ['adam', 'LISA', 'barT']
    normallist = map((lambda x:x.capitalize()), mylist)     
    print(list(normallist))
    
if __name__ == '__main__':
    main()    
    
    