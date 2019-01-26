# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:10:19 2019

请把下面的Student对象的gender字段对外隐藏起来，
用get_gender()和set_gender()代替，并检查参数有效性

@author: yangyang43
"""

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self.__gender = gender
        
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('FAILED')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('FAILED')
    else:
        print('PASSED')
     
        