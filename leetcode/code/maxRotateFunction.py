#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    """
    396.旋转函数
    """

    # 超出时间限制
    def maxRotateFunction_error(self, A):
        lst, l, index, result = [], len(A), 0, 0
        while index < l:
            if index == 0:
                newlist = A
            else:
                newlist = A[-index:] + A[0:l - index]
            for idx, val in enumerate(newlist):
                result += idx * val
            lst.append(result)
            result = 0
            index += 1
        return max(lst) if len(lst) > 0 else 0

    # 错位相减
    def maxRotateFunction(self, A):
        sum, F, ASize, maxValue = 0, 0, len(A), 0
        for i in range(ASize):
            sum += A[i]
            F += i * A[i]
        maxValue = F
        for i in range(ASize - 1, -1, -1):
            F += (sum - ASize * A[i])
            if maxValue < F:
                maxValue = F
        return maxValue


if __name__ == "__main__":
    s = Solution()
    """ 
    """
    A = [4, 3, 2, 6]
    num = s.maxRotateFunction(A)
    print(num)
    pass
