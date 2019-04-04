#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
reduce()函数，

reduce()函数也是Python内置的一个高阶函数。
reduce()函数接收的参数和 map()类似，
一个函数 f，一个list，但行为和 map()不同，
reduce()传入的函数 f 必须接收两个参数，
reduce()对list的每个元素反复调用函数f，并返回最终结果值。

reduce()还可以接收第3个可选参数，作为计算的初始值。

例如：编写一个f函数，接收x和y，返回x和y的和
"""

from functools import reduce


def f(x, y):
    return x + y


print(reduce(f, [1, 3, 5, 7, 9], 100))

"""
Python内置了求和函数sum(),但没有求积的函数，请利用reduce()来求积：

输入：[2,4,5,7,12]
"""

lst = [2, 4, 5, 7, 12]
print(sum(lst))


def prod(x, y):
    return x * y


print(reduce(prod, lst))
