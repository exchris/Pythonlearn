#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 0025 上午 10:10
# @Author  : Exchris Tsai
# @Site    : 
# @File    : example51.py
# @Software: PyCharm

"""
学习使用按位与&
程序分析:0&0=0;0&1=0; 1&0=0; 1&1=1
"""

__author__ = 'Exchris Tsai'

if __name__ == '__main__':
    a = 0o77
    b = a & 3
    print('a & b = %d' %b)
    b &= 7
    print('a & b = %d' %b)