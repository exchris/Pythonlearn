#!/bin/usr/python
# -*- coding:utf-8 -*-
# 字符串中的单词数
class Solution:

    def countSegments(self, s):
        import re
        return len(re.findall('[^\s]+', s))

s = Solution()
l = s.countSegments('Hello, my name is John')
print(l)
