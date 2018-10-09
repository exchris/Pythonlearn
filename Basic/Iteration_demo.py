#!/usr/bin/python
# coding:utf-8

"""
如果给定一个list或tuple，我们可以通过for
循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
在Python中，迭代是通过for ... in 来完成的，
而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java
代码：
"""

d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

"""
默认情况下，dict迭代的是key。
如果要迭代value，可以用for value in d.itervalues() ，
如果要同时迭代key和value，可以用for k, v in d.iteritems() 。
"""

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断:
# str是否可迭代
from _collections_abc import Iterable
print(isinstance('abc', Iterable))
# list是否可迭代
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable)) # 整数是否可迭代

# Python内置的enumerate函数可以把一个list变成索引-元素对,
# 这样就可以在for循环中同事迭代索引和元素本身
for key, value in enumerate(['A','B','C']):
    print(key, value)