#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 移动零
class Solution:
    def moveZeros(self, nums):
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums.extend([0]*n)
        print(nums)

s = Solution()
s.moveZeros([0, 0, 1, 2, 12])
# [12, 3, 1, 0, 0]
