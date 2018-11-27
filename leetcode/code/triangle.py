#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:

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


s = Solution()
s.getRow(5)
