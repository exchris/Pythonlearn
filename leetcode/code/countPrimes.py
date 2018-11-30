#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
204.计数质数
统计所以小于非负整数n的质数的数量
输入:10
输出: 4
解释:小于10的质数一共有4个，它们是2,3,5,7
"""


class Solution:

    def countPrimes(self, n):
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * len(prime[i * i:n:i])
        return sum(prime)


    def countPrimes1(self, n):
        flag, sum = False, 0
        for i in range(2, n):
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    flag = True
                    break
            if flag == 0:
                print(i)
                sum += 1
            else:
                flag = False
        print(sum)

s = Solution()
s1 = s.countPrimes1(10)
print(s1)
