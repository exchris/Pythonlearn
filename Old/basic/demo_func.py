# -*- coding:utf-8 -*-

import math

# 求解一元二次方程的解
def quadratic(a, b, c) :
  det = b*b - 4*a*c; # 判别式
  if det >= 0 :
      return (-b+math.sqrt(det))/(2*a), (-b-math.sqrt(det))/(2*a)
  else :
      return 'NaN'

print(quadratic(1,-2,1))