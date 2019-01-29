# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:28:40 2019
我们把变量从内存中变成可存储或传输的过程称之为序列化，
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，
观察该参数对结果的影响

@author: yangyang43
"""

import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
m = json.dumps(obj, ensure_ascii=False)

print(s)
print(m)