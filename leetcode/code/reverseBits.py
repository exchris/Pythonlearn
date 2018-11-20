# -*-coding:utf-8 -*-
#/bin/python

"""
颠倒给定的32位无符号整数的二进制位
示例:
	输入: 43261596
	输出: 964176192
	解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
"""
class Solution:

    # 颠倒二进制位
    def reverseBits(self, n):
        # 二进制为
        l = list('{0:032b}'.format(n))
        l = list(map(int, l))
        l.reverse()
        l = list(map(str, l))
        l = ['0', 'b'] + l
        s = ''.join(l)
        return int(s,2)


    def reverseBits1(self, n):
        s = '{0:032b}'.format(n)
        s = s[::-1]
        return int(s, 2)


s = Solution()
nums = s.reverseBits1(43261596)
print(nums)
