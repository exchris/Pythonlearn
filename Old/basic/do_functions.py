# -*- coding: utf-8 -*-

# 前100个数平方加一的和
def func2(x) :
    sum = 0
    for i in range(x + 1) :
        sum += (i**2+1)
    return sum
print(func2(100))

# 计算半径r的圆的面积
def area_of_circle(r) :
    PI = 3.1415926
    return PI*r**2
print(area_of_circle(1))
