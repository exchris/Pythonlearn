#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    """
    970.强整数
    """

    def powerfulIntegers1(self, x, y, bound):
        """
        :param x:int
        :param y: int
        :param bound:int
        :return: List[int]
        """
        res_set = set()
        for i in range(bound):
            temp1 = x ** i
            if temp1 > bound:
                break
            for j in range(bound):
                temp2 = y ** j
                temp = temp1 + temp2
                if temp > bound:
                    break
                res_set.add(temp)
        return list(res_set)

    def powerfulIntegers(self, x, y, bound):

        max, lst = 6, []
        for i in range(max + 1):
            for j in range(max + 1):
                target = x ** i + y ** j
                if target <= bound and target not in lst:
                    lst.append(target)
        return lst


if __name__ == "__main__":
    s = Solution()
    lst = s.powerfulIntegers(2, 3, 10)
    print(lst)
