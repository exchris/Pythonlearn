#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.insert(0, target)
        nums.sort()
        num = nums.index(target)
        return num