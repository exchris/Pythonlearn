# -*- coding:UTF-8 -*-
'''
reduce()函数接收的参数和map类似,一个函数f,一个list,但行为和map()不同,
reduce()传入的函数f必须接收两个参数,reduce()对list的每个元素反复调用函数f
并返回最终结果值
'''

# 编写一个f函数,接收x和y,返回x和y的和
def f(x,y):
	return x+y

print('先计算头两个元素:',f(1,3))
print('再把结果和第三个元素计算:',f(4,5))
print('再把结果和第4个元素计算:',f(9,7))
print('再把结果和第5个元素计算:',f(16,9))

from functools import reduce
# reduce()还可以接收第三个可选参数,作为计算的初始值。如果把初始值设为100,计算:
print(reduce(f,[1,3,5,7,9],100)) #125

'''
Python内置了求和函数sum(),但没有求积的函数,
请利用reduce()来求积
输入:[2,4,5,7,12]
输出:2*4*5*7*12
'''
def prod(x, y):
	return x*y

print(reduce(prod,[2,4,5,7,12]))