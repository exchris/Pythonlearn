#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    """
    832.翻转图像
    给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
    水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
    反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
    """

    def flipAndInvertImage1(self, A):
        """
        :param A:List[List[int]]
        :return: List[List[int]]
        """
        return [[j ^ 1 for j in i[::-1]] for i in A]

    def flipAndInvertImage(self, A):
        for a in A:
            a.reverse()
            for i in range(len(a)):
                if a[i] == 0:
                    a[i] = 1
                else:
                    a[i] = 0
        return A


if __name__ == "__main__":
    s = Solution()
    A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    lst = s.flipAndInvertImage(A)
    print(lst)
    pass
