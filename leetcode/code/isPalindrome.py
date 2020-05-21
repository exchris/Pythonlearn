#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([i.lower() for i in s if i.isalnum()])
        print(s)


s = Solution()
s.isPalindrome("0p")
