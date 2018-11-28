#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
507.完美数
"""

import math


class Solution:
    def checkPerfectNumber(self, num):
        if num <= 0:
            return False
        top = math.ceil(math.sqrt(num))
        nums = [1]
        for i in range(2, top):
            if num % i == 0:
                nums.append(i)
                nums.append(num / i)
        if top * top == num:
            nums.append(top)
        if sum(nums) == num:
            return True
        else:
            return False

    def checkPerfectNumber1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336
