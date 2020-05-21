# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
字母大小写全排列
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以
获得一个新的字符串，返回所有可能得到的字符串集合
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
"""


class Solution:
    def letterCasePermutation(self, S):
        """
        :param S: str
        :return: List[str]
        """
        if not S: return [S]
        rest = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]


s = Solution()
t = s.letterCasePermutation("a1b2")
print(t)
