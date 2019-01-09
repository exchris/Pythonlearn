#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
442. 数组中重复的数据

给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
"""

class Solution:

    def findDuplicates(self, nums):
        """
        :param nums:List[int]
        :return: List[int]
        """
        # return [num for num in list(set(nums)) if nums.count(num) >= 2]

        # nums.sort()
        # l = []
        # for i in range(0, len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         l.append(nums[i])
        # return l


if __name__ == "__main__":
    s = Solution()
    l = s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    print(l)
