#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:

    def getRow(self, rowIndex):
        lst = self.generate(rowIndex + 1)[-1]
        print(lst)

    def generate(self, row_nums):
        triangle = []

        for row_num in range(row_nums):
            # The first and last row elements area always 1
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

    def getRow1(self, rowIndex):
        if rowIndex == 0:
            return [1]
        lst = []
        i, j = 1, 1
        h = rowIndex
        while i < rowIndex:
            lst.append(h // j)
            h *= rowIndex - i
            j *= i + 1
            i += 1
        lst.append(1)
        lst.insert(0, 1)
        print(lst)


s = Solution()
s.getRow(5)
