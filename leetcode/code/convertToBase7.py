# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 504.七进制数

class Solution:
    def convertToBase7(self, num):
        result = ''
        abs_num = abs(num)
        if abs_num == 0:
            return "0"
        shang = int(abs_num / 7)
        result += str(abs_num % 7)
        while shang > 0:
            temp = shang
            shang = int(shang / 7)
            result += str(temp % 7)
        return result[::-1] if num > 0 else '-' + result[::-1]


s = Solution()
t = s.convertToBase7(9)
print(t)
