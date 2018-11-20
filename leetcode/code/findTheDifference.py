#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
"""
class Solution:
    def findTheDifference(self,s,t):
        sums, sumt = 0, 0
        for i in s:
            sums += ord(i)
        for i in t:
            sumt += ord(i)
        return chr(sumt - sums)

    def findTheDifferenceFirst(self, s, t):
        ch = 0
        for c in s + t:
            ch ^= ord(c)
        return chr(ch)

if __name__ == "__main__":
    s = Solution()
    str1 = s.findTheDifferenceFirst("a", "aa")
    print(str1)