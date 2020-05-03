#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
已知一个已经排好序的数组，现在输入一个数，用Python3语言按原来的规律将它插入到数组中
@author dev.erxuan@gmail.com
@file insert_sort.py
@software PyCharm
@date 2020/4/20 23:31
"""
list_1 = [1, 2, 3, 4, 5, 6, 7]
num_1 = int(input("input = ?"))
for i, v in enumerate(list_1):
    if num_1 < v:
        list_1.insert(i, num_1)
        break
print(list_1)
if __name__ == "__main__":
    pass
