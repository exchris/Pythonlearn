#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

""""
Python内置的sorted()函数可对list进行排序
"""
print(sorted([36, 5, 12, 9, 21]))

"""
但sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，
传入两个待比较的元素x,y，如果x应该排在y的前面，返回-1,如果x应该排在y的后面，返回1，
如果x和y相等，返回0
"""

def cmp_ignore_case(x):
    return x.upper()


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=cmp_ignore_case))
