# -*- coding:UTF-8 -*-
'''
Created on 2017年7月19日

@author: Administrator
'''
# 计算数列1 4 7 10 13 16 19前100项的和
x1 = 1
d = 3
n = 100
x100 = x1 + (n-1)*d
s = n*(x1+x100)/2
print(s)