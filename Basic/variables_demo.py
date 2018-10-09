#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 不可变对象

# str是不变对象，而list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)

# 而对于不可变对象，比如str,对str进行操作:
a = 'abc'
print(a.replace('a', 'A'))
print(a)
