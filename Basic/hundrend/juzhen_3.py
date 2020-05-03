#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
Python3语言，求一个3*3矩阵主对角线元素之和
@author dev.erxuan@gmail.com
@file juzhen_3.py
@software PyCharm
@date 2020/4/20 23:34
"""
sum_1 = 0
matrix = [[2, 3, 6], [8, 6, 4], [5, 3, 2]]
for i in range(len(matrix)):
    sum_1 += matrix[i][i]
print(sum_1)

if __name__ == "__main__":
    pass
