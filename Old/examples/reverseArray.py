"""
Created on 八月 03 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-

# 已知数组python列表a = [99,66,25,10,3],并且是已经排序过的。现在要求,将a数组的元素逆向排序
a = [99,66,25,10,3]
if __name__ == "__main__":
    N = len(a)
    print(a)
    print(len(a)/2)
    for i in range(len(a)//2):
        a[i],a[N-i-1] = a[N-i-1],a[i]
    print(a)

