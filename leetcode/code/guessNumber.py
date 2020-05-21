#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 374.猜数字大小

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min1, max1 = 1, n
        while (1):
            tmp = (min1 + max1) / 2
            flag = guess(tmp)
            if flag == 1:
                min1 = tmp
            elif flag == -1:
                max1 = tmp
            else:
                return tmp
            if max1 - min1 == 1:
                if flag == 1:
                    return max1
                else:
                    return min1
