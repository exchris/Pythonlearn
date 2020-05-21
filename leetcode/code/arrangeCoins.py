#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'
class Solution:
    """
    441.排列硬币
    """
    def arrangeCoins(self, n):
        """
        :param n:int
        :return: int
        """
        x = 0
        sum = 0
        while True:
            sum = sum + x + 1
            if sum > n:
                break
            x += 1
        print(x)
if __name__ == "__main__":
    s = Solution()
    """ 
    """
    n = 10
    s.arrangeCoins(n)
    pass
