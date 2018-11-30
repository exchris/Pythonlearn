#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def plusOne(self, digits):
        s , output = '', []

        for i in digits:
            s += str(i)
        num = int(s) + 1
        for i in str(num):
            output.append(int(i))
        print(output)

s = Solution()
s.plusOne([9, 9])