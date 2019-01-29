# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:51:28 2019

请尝试写一个验证Email地址的正则表达式。

版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com

版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob

@author: yangyang43
"""

import re
def is_valid_email(addr):
    re_email = re.compile(r'\w+.\w+@\w+.\w+')
    if re.match(re_email, addr):
        return True
    else: 
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com' ) 
print ('OK')

def name_of_email(addr):
    re_name = re.compile(r'^<?([\w\s]*)>?[\s\w]*@\w+.\w+')
    return re.match(re_name, addr).group(1)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')