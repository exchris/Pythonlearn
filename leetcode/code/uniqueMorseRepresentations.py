#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def uniqueMorseRepresentations(self, words):
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        lst = []
        for word in words:
            s = ''
            for w in word:
                n = ord(w) - 97
                s += arr[n]
            lst.append(s)
        print(len(set(lst)))


s = Solution()
s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
