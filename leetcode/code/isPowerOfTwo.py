#!/usr/bin/python
# -*- coding:utf-8 -*-

# 2的幂
class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True

        while n > 1:
            if (n % 2 != 0):
                return False
            n /= 2
        return True
    
s = Solution()
b = s.isPowerOfTwo(1)
print(b)