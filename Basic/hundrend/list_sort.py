#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
Python3编程，对10个数进行倒序排序（不能使用sort函数）
@author dev.erxuan@gmail.com
@file list_sort.py
@software PyCharm
@date 2020/4/20 23:36
"""
n_1 = []
for i in range(0, 10):
    num = float(input("number=?"))
    n_1.append(num)
for j in range(0, 10):
    for k in range(j+1, 10):
        if n_1[j] < n_1[k]:
            n_1[j],n_1[k] = n_1[k],n_1[j]
print(n_1)

if __name__ == "__main__":
    pass
