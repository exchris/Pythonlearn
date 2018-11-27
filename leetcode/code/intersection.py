#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution:
    """
    349.两个数组的交集
    """

    def intersection(self, nums1, nums2):
        lst = list(set(nums1) & set(nums2))
        print(lst)

s = Solution()
s.intersection([1, 2, 2, 1], [2, 2])
