#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def fib(self, N):
        """
        :param N:int
        :return: int
        """
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)


if __name__ == "__main__":
    s = Solution()
    num = s.fib(4)
    print(num)
