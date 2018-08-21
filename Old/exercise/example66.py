#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 0025 下午 3:56
# @Author  : Exchris Tsai
# @Site    : 
# @File    : example66.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

# 题目: 输入3个数a,b,c,按大小顺序输出

if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))

    def swap(p1, p2):
        return p2, p1

    if n1 > n2 : n1, n2 = swap(n1, n2)
    if n1 > n3 : n1, n3 = swap(n1, n3)
    if n2 > n3 : n2, n3 = swap(n2, n3)

    print(n1, n2, n3)


    # 使用sort()
    a = []

    for i in range(3):
        a.append(int(input('请输入一个数字:')))

    a.sort()
    print(a)

    # remove

    l=[]
    for i in range(3):
        x=input('输入一个数字:')
        l.append(x)
    for i in range(3):
        print(max(l))
        l.remove(max(l))  #利用 remove（）函数依次输出最大值

    L = []
    for i in range(3):
        L.append(int(input('输入一个数字:')))
    for i in range(3):
        for j in range(i + 1, 3):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    print(L)
