# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 1012.十进制整数的反码

class Solution:

    def bitwiseComplement(self, N):
        b = bin(N)[2:]
        str1 = ''
        for i in b:
            if i == '0':
                str1 += '1'
            else:
                str1 += '0'
        print(int(str1, 2))

if __name__ == "__main__":
    s = Solution()
    s.bitwiseComplement(5)
