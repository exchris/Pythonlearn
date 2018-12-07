#!/bin/usr/python
# -*- coding:utf-8 -*-
class Solution:
    def sortColors1(self, nums):
        count0 = nums.count(0)
        count1 = nums.count(1)
        i = 0
        while i < count0:
            nums[i] = 0
            i += 1
        while i < count0 + count1:
            nums[i] = 1
            i += 1
        while i < len(nums):
            nums[i] = 2
            i += 1
        print(nums)

    def sortColors(self, nums):
        n = len(nums)

        lt = -1
        gt = n
        i = 0

        while i < gt:
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1
        print(nums)


s = Solution()
nums = [2, 0, 2, 1, 1, 0]
s.sortColors(nums)

