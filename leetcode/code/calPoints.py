# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 682 棒球比赛
class Solution:
    def calPoints(self, ops):
        """
        :param ops:List[str]
        :return: int
        """
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)


s = Solution()
t = s.calPoints(["5", "2", "C", "D", "+"])
print(t)
