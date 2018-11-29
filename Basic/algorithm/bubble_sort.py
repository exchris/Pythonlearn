#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:

    def bubble_sort(self, nums):
        for i in range(1, len(nums)):
            for j in range(0, len(nums) - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


s = Solution()
lst = s.bubble_sort([2, 3, 1, 4, 5, 9, 8])
print(lst)
