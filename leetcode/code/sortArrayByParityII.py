#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    """
    922.按奇偶排序数组II
    """

    def sortArrayByParityII(self, A):
        """
        :param A:List[int]
        :return: List[int]
        """
        even = [i for i in A if i % 2]
        odd = [i for i in A if not i % 2]

        return [i for n in zip(odd, even) for i in n]


if __name__ == "__main__":
    s = Solution()
    A = [4, 2, 5, 7]
    lst = s.sortArrayByParityII(A)
    print(lst)
    pass
