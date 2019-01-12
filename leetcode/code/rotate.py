#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def rotate1(self, matrix):
        """
        :param matrix:List[List[int]]
        :return:void
        """
        l = len(matrix)
        t = []
        for i in range(l):
            t1 = []
            for j in range(l):
                t1.append(matrix[l - 1 - j][i])
            t.append(t1)
        print(t)
    def rotate2(self, matrix):
        matrix[:] = map(list, zip(*matrix[::-1]))

    def rotate(self, matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(i + 1, length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(length):
            matrix[i] = matrix[i][::-1]
        print(matrix)


if __name__ == "__main__":
    s = Solution()
    """ 
    """
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    lst = s.rotate(matrix)
    print(lst)
    pass
