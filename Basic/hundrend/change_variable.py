#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
请使用Python3语言，用四种方法将两个变量的值互换位置。比如将a=3, b=4，互换后变成a=4, b=3
@author dev.erxuan@gmail.com
@file change_variable.py
@software PyCharm
@date 2020/4/20 23:22
"""
def one(x, y):
    x, y = y, x
    return x, y

def two(x, y):
    t = [x, y]
    t_1 = t[::-1]
    return  t_1

def three(x, y):
    t = x
    x = y
    y = t
    return x, y

def four(x, y):
    z = x + y
    x = z - x
    y = z - y
    return x, y

if __name__ == "__main__":
    pass
