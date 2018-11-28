#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        else:
            return nums.index(target)

    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1

        # while you haven't narrowed it down to one element ...
        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            guess = nums[mid]
            # Found the item.
            if guess == target:
                return mid
            # The guess was too high.
            if guess > target:
                high = mid - 1
            # the guess was too low.
            else:
                low = mid + 1
        # Item doesn't exist
        return -1


s = Solution()
index = s.binary_search([-1, 0, 3, 5, 9, 12], 9)
print(index)
