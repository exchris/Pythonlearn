# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 278.第一个错误的版本

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high: #等号
            mid = (low + high) // 2
            nowRes = isBadVersion(mid)
            if nowRes:
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:low = mid + 1

