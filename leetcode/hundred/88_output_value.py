#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(input('input a number:\n'))
        print(a * '*')
        n += 1
