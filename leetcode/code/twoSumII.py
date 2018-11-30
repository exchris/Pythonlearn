#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:

    # 超出时间限制
    def twoSum1(self, numbers, target):
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return [-1, -1]

    # 超出时间限制
    def twoSum2(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1, i, -1):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return [-1, -1]

    # 超出时间限制
    def twoSum3(self, numbers, target):
        for i in range(len(numbers) - 1):
            t = target - numbers[i]
            if t in numbers:
                numbers.pop(i)
                return [i + 1, numbers.index(t) + 2]
        return [-1, -1]

    def twoSum(self, numbers, target):
        s, r = {}, []
        for i in range(len(numbers)):
            if numbers[i] in s.keys():
                print(numbers[i])
                r.append(s[numbers[i]] + 1)
                r.append(i + 1)
                return r
            s[target - numbers[i]] = i
        return None

    def twoSum4(self, numbers, target):
        """
                :type numbers: List[int]
                :type target: int
                :rtype: List[int]
                """
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []


s = Solution()
lst = s.twoSum([0, 0, 3, 4], 0)
print(lst)
