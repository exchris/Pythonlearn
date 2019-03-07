#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 345.反转字符串种的元音字符

# 使用双指针指向待反转的两个元音字符，一个指针从头向尾遍历，一个指针从尾到头遍历
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s) - 1
        result = [0 for _ in range(len(s))]
        print(result)
        while i <= j:
            ci = s[i]
            cj = s[j]
            if ci not in vowels:
                result[i] = ci
                i += 1
            elif cj not in vowels:
                result[j] = cj
                j -= 1
            else:
                result[i] = cj
                i += 1
                result[j] = ci
                j -= 1
        print(''.join(result))

s = Solution()
s.reverseVowels("leetcode")
