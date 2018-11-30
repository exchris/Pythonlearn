#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 383.打乱数组
class Solution:

    def __init__(self, nums):
        self.origin = nums[:]
        self.output = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        n = len(self.output)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output


nums = [1, 2, 3]
s = Solution(nums)
print(s.shuffle())
print(s.reset())
