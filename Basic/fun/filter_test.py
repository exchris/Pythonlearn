#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
filter()函数是 Python 内置的另一个有用的高阶函数，

filter()函数接收一个函数 f 和一个list，
这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

例如：要从一个list[1,4,6,7,9,12,17]中删除偶数，保留奇数，首先，要编写一个判断奇数的函数：
"""


def is_odd(x):
    return x % 2 == 1


# 然后，利用filter()过滤掉偶数：
print(list(filter(is_odd, [1, 4, 6, 7, 9, 12, 17])))

# 利用列表生成式
print([x for x in [1, 4, 6, 7, 9, 12, 17] if x % 2])


# 利用filter(),可以完成很多有用的功能，例如，删除None或者空字符串
def is_not_empty(s):
    return s and len(s.strip()) > 0


# s.strip(rm)删除s字符串中开头、结尾处的rm序列的字符，当rm为空时，默认删除空白符（包括'\n','\r','\t',''）
print(list(filter(is_not_empty, ['test', None, '', 'str', '', 'END'])))

import math


def is_number(x):
    b = int(math.sqrt(x))
    return b * b == x

# 利用filter()过滤出1~100中平方根是整数的树
print(list(filter(is_number, [x for x in range(1, 101)])))
