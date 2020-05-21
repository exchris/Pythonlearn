#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    """
    824. 山羊拉丁文
    - 如果单词以元音开头（a, e, i, o, u），在单词后添加"ma"。
        例如，单词"apple"变为"applema"。

    -   如果单词以辅音字母开头（即非元音字母），移除第一个字符并将它放到末尾，之后再添加"ma"。
        例如，单词"goat"变为"oatgma"。

    -   引相同数量的字母'a'，索引从1开始。
        例如，在第一个单词后添加"a"，在第二个单词后添加"aa"，以此类推
    """

    def toGoatLatin(self, S):
        """
        :param S: str
        :return: str
        """
        lsts = S.split(" ")
        print(lsts)
        newlsts = []
        l = len(lsts)
        for i in range(l):
            if lsts[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                s = lsts[i] + 'ma' + 'a' * (i + 1)
            else:
                s = lsts[i][1:] + lsts[i][0] + 'ma' + 'a' * (i + 1)
            newlsts.append(s)
        print(" ".join(newlsts))


s = Solution()
s.toGoatLatin("The quick brown fox jumped over the lazy dog")
