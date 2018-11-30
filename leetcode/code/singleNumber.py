#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 137.只出现一次的数字II
class Solution:

    def singleNumber(self, nums):
        a, b = 0, 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b

s = Solution()
s1 = s.singleNumber([2, 2, 3, 2])
print(s1)