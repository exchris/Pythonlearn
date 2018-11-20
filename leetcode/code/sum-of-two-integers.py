#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
"""
import datetime
class Solution:
    def getSum(self, a, b):
        """
        :param a:int
        :param b: int
        :return: int
        """
        return a + b

if __name__ == "__main__":
    s = Solution()
    num = s.getSum(-2, 0)
    print(num)