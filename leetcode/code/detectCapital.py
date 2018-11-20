#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
"""

import time
class Solution:
    def detectCapitalUse(self, word):
        """
        :param word: str
        :return: bool
        """
        if word.isupper():
            return True
        elif word.capitalize() == word:
            return True
        elif word.islower():
            return True
        else:
            return False

    def detectCapitalUseFirst(self, word):
        """
        :param word:str
        :return: bool
        """
        return word.islower() or word.isupper() or word.istitle() or word == ''

    def detectCapitalUseSecond(self, word):
        """
        :type word: str
        :rtype: bool
        """
        test = word.upper()
        test1 = word.lower()
        if test == word or test1 == word:
            return True
        for i in range(1, len(word)):
            if word[i] == test[i]: return False
        return True
    def detectCapitalUseThird(self, word):
        """
        :param word:str
        :return:bool
        """
        n = len(word)
        if n == 1:return True
        if word[0] < 'a':
            if n == 2:return True
            if word[1] < 'a':
                for i in range(2, n):
                    if word[i] >= 'a':
                        return False
            else:
                for i in range(2, n):
                    if word[i] < 'a':
                        return False
        else:
            for i in range(1, n):
                if word[i] < 'a':
                    return False
        return True

if __name__ == "__main__":
    start = time.clock()
    s = Solution();
    word = ['USA', 'FlaG', 'g', 'leetcode', 'Usa']
    for i in word:
        print(s.detectCapitalUseThird(i))
    end = time.clock()
    print(end-start)
