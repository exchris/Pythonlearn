#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 将整数数字转换为字符数组
        s = [str(i) for i in digits]
        result = int("".join(s))
        result += 1
        l = len(str(result))
        lst = []
        i = 0
        while i < l:
            p = result % 10
            lst.append(p)
            result //= 10
            i += 1
        print(lst[::-1])


s = Solution()
digits = [99]
s.plusOne(digits)
