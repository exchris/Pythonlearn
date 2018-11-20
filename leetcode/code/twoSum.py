#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :param nums:List[int]
        :param target: int
        :return: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
        return [-1, -1]

    def twoSumTwo(self, nums, target):
        # 用len()方法取得nums列表长度
        n = len(nums)
        # x从0到n取值(不包括n)
        for x in range(n):
            a = target - nums[x]
            # 用in关键字查询nums列表中是否有a
            if a in nums:
                # 用index函数取得a的值在nums列表中的索引
                y = nums.index(a)
                # 假如x=y,那么久跳过，否则返回x,y
                if x == y:
                    continue
                else:
                    return x,y
                    break
            else:
                continue

    def twoSumThree(self, nums, target):
        # 用len()方法取得nums列表长度
        n = len(nums)
        # 创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]], x
            # 否则往字典增加键值对
            else:
                d[a] = x

s = Solution()
lst = s.twoSumThree([3,3], 6)
print(lst)