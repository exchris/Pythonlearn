#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
46.全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums):
        if [] == nums:
            return [[]]

        outcome = []
        self.core(nums, 0, outcome)
        return outcome

    def core(self, nums, left, outcome):
        if left == len(nums) - 1:
            outcome.append(nums[:])
        else:
            for i in range(left, len(nums)):
                if i == left:
                    self.core(nums, left + 1, outcome)
                else:
                    nums[left], nums[i] = nums[i], nums[left]
                    self.core(nums, left + 1, outcome)
                    nums[left], nums[i] = nums[i], nums[left]


if __name__ == "__main__":
    s = Solution()
    outcome = s.permute([1, 2, 3])
    print(outcome)
