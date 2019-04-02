#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ :exchris


class Solution:
    def distributeCandies(self, candies):
        return min(len(set(candies)), len(candies) // 2)


s = Solution()
t = s.distributeCandies([1,1,2,3])
print(t)
