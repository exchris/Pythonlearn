# -*- coding:UTF-8 -*-
'''
定义一个函数,接受x,y,f三个参数
其中x,y是数值,f是函数
def add(x,y,f):
    return f(x) + f(y)
'''
def add(x,y,f):
	return f(x)+f(y)

print(add(-5,9,abs)) # 14

# 利用add(x,y,f)函数,计算:math.sqrt(x)+math.sqrt(y)

import math
print(add(25,9,math.sqrt)) # 8.0