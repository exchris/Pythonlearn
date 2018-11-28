#!/bin/usr/python
# -*- coding:utf-8 -*-
# 628.三个数的最大乘积
class Solution:

    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        elif len(nums) < 3:
            return None
        else:
            z_num, f_num = [], []
            for i in nums:
                if i < 0:
                    f_num.append(i) # 负数列表
                else:
                    z_num.append(i) # 正数列表
            z_num.sort(reverse=True)
            f_num.sort()
            sum1, sum2 = 1, 1
            if len(f_num) < 2:
                return z_num[0] * z_num[1] * z_num[2]
            elif len(z_num) < 2:
                return f_num[0] * f_num[1] * z_num[0]
            else:
                sum2 *= f_num[0]
                sum2 *= f_num[1]
                sum2 *= z_num[0]

                sum1 *= z_num[0]
                sum1 *= z_num[1]
                sum1 *= z_num[2]
                return max(sum1, sum2)

s = Solution()
num = s.maximumProduct([-4, -3, -2, -1, 60])
print(num)



