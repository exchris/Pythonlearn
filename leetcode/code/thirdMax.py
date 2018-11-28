#!/bin/usr/python
# -*- coding:utf-8 -*-
class Solution:
    def thirdMax(self, nums):
        lst = list(set(nums))
        lst.sort(reverse=1)
        if len(lst) < 3:
            return max(lst)
        else:
            return lst[2]


s = Solution()
num = s.thirdMax([3, 2, 1])
print(num)

num = s.thirdMax([1, 2])
print(num)

num = s.thirdMax([2, 2, 3, 1])
print(num)
