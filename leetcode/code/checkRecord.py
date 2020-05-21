#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    """
    551.学生出勤记录
    给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

        'A' : Absent，缺勤
        'L' : Late，迟到
        'P' : Present，到场
    如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
    """

    def checkRecord(self, s):
        """
        :param s:str
        :return: book
        """
        b = s.count('A') <= 1 and s.count('LLL') == 0
        print(b)


if __name__ == "__main__":
    s = Solution()
    s.checkRecord("LALL")
