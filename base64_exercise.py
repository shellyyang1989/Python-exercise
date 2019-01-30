# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:32:49 2019

Base64是一种任意二进制到文本字符串的编码方法，
常用于在URL、Cookie、网页中传输少量二进制数据。
Base64编码后会把=自动去掉：
请写一个能处理去掉=的base64解码函数

@author: yangyang43
"""

import base64
def safe_base64_decode(s):
    return base64.b64decode(s+(4-len(s)%4)*b"=")    

assert b'abcd' == safe_base64_decode(b'YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA')
print('ok')