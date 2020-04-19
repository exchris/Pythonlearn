#!/bin/usr/python
# -*-coding:utf-8-*-

class Solutin:

    def test(self, nums, k):
        l = len(nums)
        t = l - k
        nums[t:], nums[0:t] = nums[0:t], nums[t:]
        print(nums)


# 5,6,7 4:
# 1 2 3 4 0:3

if __name__ == "__main__":
    s = Solutin()
    nums = [1, 2, 3]
    k = 4
    s.test(nums, k)
