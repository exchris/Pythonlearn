# -*- coding:UTF-8 -*-
'''
Created on 2017年7月19日

@author: Administrator
'''
import math

def quadratic_equation(a, b, c):
    de = b*b - 4*a*c
    if de >= 0 :
        x1 = (-b+math.sqrt(de))/(2*a)
        x2 = (-b-math.sqrt(de))/(2*a)
        return x1,x2
    else:
        return

print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))