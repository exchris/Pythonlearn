#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 771.宝石与石头
class Solution:

    def numJewelsInStones1(self, J, S):
        count = 0
        for i in S:
            for j in J:
                if j == i:
                    count += 1
        return count

    def numJewelsInStones2(self, J, S):
        count = 0
        for i in J:
            count += S.count(i)
        print(count)


s = Solution()
t = s.numJewelsInStones("z", "ZZ")
print(t)