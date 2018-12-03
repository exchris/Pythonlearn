#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def __init__(self):
        self.base = {4, 16, 37, 58, 145, 42, 20}

    def isHappy(self, n):
        sums = sum(map(lambda x: x ** 2, map(int, str(n))))
        if sums in self.base:
            return False
        if sums != 1:
            return self.isHappy(sums)
        else:
            return True
