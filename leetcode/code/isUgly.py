#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 263.丑数(只包含2,3,5的正整数)
class Solution:
    def isUgly(self, num):
        if num < 1:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return (num == 1) or (num == 2) or (num == 3) or (num == 5)

    # 因式分解
    def getFactory(self, num):
        return [x for x in range(1, num+1) if num % x == 0]


s = Solution()
b = s.getFactory(28)
print(b)
