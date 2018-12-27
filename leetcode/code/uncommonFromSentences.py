#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:

    def uncommonFromSentences(self, A, B):
        C = A + " " + B
        T = C.split(" ")
        return [i for i in T if T.count(i) == 1]


s = Solution()
A = "this apple is sweet"
B = "this apple is sour"
C = s.uncommonFromSentences(A, B)
print(C)
