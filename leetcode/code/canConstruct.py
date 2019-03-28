# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        借助字典实现
        :param ransomNote:
        :param magazine:
        :return:
        """
        d = {}
        for i in magazine:
            d[i] = d.get(i, 0) + 1
        for i in ransomNote:
            d[i] = d.get(i, 0) - 1
            if d[i] < 0:
                return False
        return True

if __name__ == "__main__":

    s = Solution()
    b = s.canConstruct("aa", "aa")
    print(b)
