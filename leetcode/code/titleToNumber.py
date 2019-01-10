#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def titleToNumber(self, s):
        """
        :param s:str
        :return: int
        """
        number, t = 0, 0
        if len(s) == 1:
            number = ord(s) - 64
        else:
            for i in s[::-1]:
                number += (ord(i) - 64) * 26 ** t
                t += 1
        print(number)


if __name__ == "__main__":
    s = Solution()
    t = s.titleToNumber('ZY')
    pass
