#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 0028 上午 11:21
# @Author  : Exchris Tsai
# @Site    : 
# @File    : fileread.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import io

f = open('exchris.txt')
list_c = f.readline()

list_cs1 = f.readlines(1)
print(len(list_cs1))
print(io.DEFAULT_BUFFER_SIZE)


"""
readline(size)
  len(line) > size return size
  len(line) < size return len(line)
"""
