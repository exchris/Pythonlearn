#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

示例 1:

输入: L = 6, R = 10
输出: 4
解释:
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
示例 2:

输入: L = 10, R = 15
输出: 5
解释:
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)
注意:

L, R 是 L <= R 且在 [1, 10^6] 中的整数。
R - L 的最大值为 10000。
"""

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :param L:int
        :param R: int
        :return: int
        """
        count = 0
        for num in range(L, R + 1):
            zhiwei = self.countNum(num)
            if self.isPrime(zhiwei):
                count += 1
            else:
                continue
        return count

    # 判断是否为质数
    def isPrime(self, num):
        if num > 1:
            # 查看因子
            for i in range(2, num):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

    # 计算整数的二进制置位
    def countNum(self, num):
        b = bin(num)[2:]
        count = 0
        for i in b:
            if i == '1':
                count += 1
            else:
                continue
        return count

    def countPrimeSetBitsFirst(self, L, R):
        """
        :param L: int
        :param R: int
        :return: int
        """
        set_bits = [2,3,5,7,11,13,17,19]
        num = 0
        for i in range(L, R + 1):
            res = bin(i).count('1')
            if res in set_bits:
                num += 1
        return num

    def countPrimeSetBitsSecond(self, L, R):
        """
        :param L:int
        :param R: int
        :return: int
        """
        # L,R是在[1,10^6]中的整数，因此置位的个数最多为19
        # 创建类别p,0-20中质数为置1，非质数置为0
        p = (0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1)
        re = 0
        for n in range(L, R + 1):
            re += p[bin(n).count('1')]
        return re

if __name__ == "__main__":
    s = Solution()
    num = s.countPrimeSetBitsSecond(6, 10)
    print(num)