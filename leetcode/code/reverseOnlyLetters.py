#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        p = [i for i in S if i.isalpha()]
        lst = ''.join([i if not i.isalpha() else p.pop() for i in S])
        print(lst)


s = Solution()
T = "a-bC-dEf-ghIj"
s.reverseOnlyLetters(T)
