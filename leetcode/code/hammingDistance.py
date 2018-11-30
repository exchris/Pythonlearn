#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 461.汉明距离
class Solution:
    def hammingDistance(self, x, y):
        s = bin(x ^ y)[2:]
        print(s.count('1'))

s = Solution()
s.hammingDistance(1, 4)