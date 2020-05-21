#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:

    def nthUglyNumber(self, number):
        count, n = 0, 1
        while True:
            if self.isUgly(n):
                count += 1
            if count == number:
                return n
            else:
                n += 1

    def isUgly(self, number):
        while number % 2 == 0:
            number = number / 2
        while number % 3 == 0:
            number = number / 3
        while number % 5 == 0:
            number = number / 5
        if number == 1:
            return True
        else:
            return False

    def findKthUgly(self, k):
        ugly = []
        ugly.append(1)
        index, index2, index3, index5 = 1, 0, 0, 0
        while index < k:
            val = min(ugly[index2] * 2, ugly[index3] * 3, ugly[index5] * 5)
            if ugly[index2] * 2 == val:
                index2 += 1
            if ugly[index3] * 3 == val:
                index3 += 1
            if ugly[index5] * 5 == val:
                index5 += 1
            ugly.append(val)
            index += 1
        return ugly[-1]


s = Solution()
t = s.findKthUgly(12)
print(t)
