#!/usr/bin/python
# -*- coding:utf-8 -*-

# 整数反转
class Solution:
    def reverse(self, x):
        if x >= 0:
            num = int(str(x)[::-1])
        else:
            num = int('-' + str(-x)[::-1])

        if num >= (-2 ** 31) and num <= 2 ** 31 - 1:
            return num
        else:
            return 0


s = Solution()
n = s.reverse(123)
print(n)

n = s.reverse(-123)
print(n)

n = s.reverse(120)
print(n)

n = s.reverse(1563847412)
print(n)
