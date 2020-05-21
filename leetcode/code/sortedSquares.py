#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 0:
            return []
        p = [x ** 2 for x in A]
        p.sort()
        return p

        # return sorted([x*x for x in A])

if __name__ == "__main__":
    s = Solution()
    A = [-4, -1, 0, 3, 10]
    t = s.sortedSquares(A)
    print(t)
