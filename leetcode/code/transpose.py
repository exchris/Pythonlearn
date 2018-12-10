#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:

    def transpose1(self, A):
        n = []
        for i in range(len(A)):
            n.append(len(A[i]))
        m = max(n)
        l = []
        for i in range(m):
            t = []
            for j in range(len(A)):
                t.append(A[j][i])
            l.append(t)
        return l

    def transpose(self, A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


s = Solution()
A = [[1, 2, 3], [4, 5, 6]]
p = s.transpose(A)
print(p)
