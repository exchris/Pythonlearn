# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def convertToTitle(self, n):
        # 1 -> A
        # 26 -> Z
        # 28 -> AB
        lst = []
        while n:
            mod = n % 26
            n //= 26
            if mod == 0:
                mod = 26
                n -= 1
            lst.append(mod)
        return ''.join([chr(i + 64) for i in reversed(lst)])


if __name__ == '__main__':
    s = Solution()
    t = s.convertToTitle(701)
    print(t)
    pass
