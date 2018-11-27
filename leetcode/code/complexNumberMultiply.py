#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    # 复数乘法
    def complexNumberMultiply(self, a, b):
        # 获得字符串a的实数部分
        a_real = a.replace('i', '').split('+')[0]
        a_imag = a.replace('i', '').split('+')[1]
        int_a_real = int(a_real)
        int_a_imag = int(a_imag)

        b_real = b.replace('i', '').split('+')[0]
        b_imag = b.replace('i', '').split('+')[1]
        int_b_real = int(b_real)
        int_b_imag = int(b_imag)

        s1 = str(int_a_real * int_b_real)
        s2 = str(int_a_real * int_b_imag + int_b_real * int_a_imag) + 'i'
        s3 = str(int_b_imag * int_a_imag)
        less = int(s1) - int(s3)
        s = str(less) + '+' + s2
        print(s)

    def complexNumberMultiply1(self, a, b):
        A, B = [], []
        for x in a.replace('i', '').split('+'):
            A.append(int(x))
        for x in b.replace('i', '').split('+'):
            B.append(int(x))

        s = str(A[0] * B[0] - A[1] * B[1]) + '+' + str(A[0] * B[1] + A[1] * B[0]) + 'i'
        print(s)


s = Solution()
s.complexNumberMultiply1("1+-1i", "1+-1i")
