#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def addToArrayForm(self, A, K):
        """
        :param A:List[int]
        :param K:int
        :return: List[int]
        """
        sa = ''
        for i in A:
            sa += str(i)
        int_sa = int(sa)
        rst = int_sa + K
        l = []
        for i in str(rst):
            l.append(int(i))
        print(l)


if __name__ == '__main__':
    s = Solution()
    A = [9, 9, 9, 9, 9, 9, 9, 9]
    K = 1
    s.addToArrayForm(A, K)
