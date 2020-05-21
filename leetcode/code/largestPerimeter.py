#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'
class Solution:
    """
    976.三角形的最大周长
    """

    def largestPerimeter(self, A):
        """
        :param A:List[int]
        :return: int
        """
        if A is None or len(A) < 3:
            return 0
        A.sort()
        max = 0
        for i in range(2, len(A)):
            curSum = A[i] + A[i - 1] + A[i - 2]
            if A[i] * 2 < curSum:
                if curSum > max:
                    max = curSum
        return max


if __name__ == "__main__":
    s = Solution()
    """ 
    """
    A = [2, 1, 3]
    num = s.largestPerimeter(A)
    print(num)
    pass
