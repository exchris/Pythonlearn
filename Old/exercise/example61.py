#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 0025 下午 3:42
# @Author  : Exchris Tsai
# @Site    : 
# @File    : example61.py
# @Software: PyCharm

# 题目：打印出杨辉三角形（要求打印出10行如下图）。
__author__ = 'Exchris Tsai'

if __name__ == '__main__':
    num = int(input('输入杨辉三角行数:\n'))
    a = []
    for i in range(num):
        a.append([])
        for j in range(num):
            a[i].append(0)

    for i in range(num):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, num):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    from sys import stdout
    for i in range(num):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print()
