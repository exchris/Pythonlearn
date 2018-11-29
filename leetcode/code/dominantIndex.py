#!/bin/usr/python
# -*- coding:utf-8 -*-
# 747.至少是其他数字两倍的最大数
class Solution:

    def dominantIndex(self, nums):
        maxnumber = max(nums)
        index = nums.index(maxnumber)  # 最大值得索引值
        m = 0
        for i in range(len(nums)):
            if nums[i] < maxnumber and nums[i] > m:
                m = nums[i]
            else:
                continue
        if maxnumber >= 2 * m:
            return index
        else:
            return -1

s = Solution()
num = s.dominantIndex([3, 6, 1, 0])
print(num)
