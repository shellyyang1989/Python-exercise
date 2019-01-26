# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:09:12 2019

为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
因为实例初始化时会调用__init__，所以要让类属性自动增加，需要在实力初始化方法中
对类属性+1

@author: yangyang43
"""
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
     
if Student.count != 0:
    print('FAILED')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('FAILED')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('FAILED')
        else:
            print('Students:', Student.count)
            print('PASSED')        