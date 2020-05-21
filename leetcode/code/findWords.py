# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 500. 键盘行

class Solution:

    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx <= set1 or setx <= set2 or setx <= set3:
                res.append(i)

        return res


if __name__ == "__main__":
    s = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    s.findWords(words)
