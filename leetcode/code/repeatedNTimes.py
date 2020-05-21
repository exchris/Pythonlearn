#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 961 重复N次的元素

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        n = len(A)
        for a in A:
            lookup[a] += 1
            if lookup[a] == n // 2:
                print(a)


A = [1, 2, 3, 3]
s = Solution()
s.repeatedNTimes(A)
