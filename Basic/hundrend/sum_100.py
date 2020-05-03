#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
使用Python3语言编程，用三种办法计算1+2+3+4+...+99+100的和
@author dev.erxuan@gmail.com
@file sum_100.py
@software PyCharm
@date 2020/4/20 22:40
"""
def one():
    sum = sum(x for x in range(101))
    return sum

def two():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum

def three(n):
    if n <= 1:
        return 1
    else:
        return n + three(n - 1)

if __name__ == "__main__":
    pass
