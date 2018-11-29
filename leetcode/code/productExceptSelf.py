#!/bin/usr/python
# -*- coding:utf-8 -*-
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp1 = [1]
        dp2 = [1]
        for i in range(len(nums) - 1):
            dp1.append(dp1[i] * nums[i])
            dp2.append(dp2[i] * nums[-i - 1])

        output = []
        for i in range(len(dp1)):
            output.append(dp1[i] * dp2[-i - 1])
        return output

s = Solution()
lst = s.productExceptSelf([1, 2, 3, 4])
print(lst)
