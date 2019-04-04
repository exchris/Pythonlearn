#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
匿名函数 lambda

关键字lambda表示匿名函数，冒号前面的x表示函数参数

匿名函数有个限制，就是只能有一个表达式，不写return,返回值就是表达式的结果
"""
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print(list(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', ' ', 'END'])))
