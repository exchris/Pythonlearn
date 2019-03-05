# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
34.在排序数组中查找元素的第一个和最后一个位置
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        if not nums:
            return [-1, -1]

        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            l = -1
        r = bisect.bisect_right(nums, target) - 1
        if nums[r] != target:
            r = -1

        return [l, r]


if __name__ == "__main__":
    S = Solution()
    lst = S.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(lst)
