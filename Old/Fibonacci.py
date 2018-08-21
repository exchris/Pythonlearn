# -*- coding:utf-8 -*-
# 斐波那契数列, 输出第10个斐波那契数列

# 方法一
def fib(n):
	a, b = 1, 1
	for i in range(n - 1):
		a, b = b, a + b
	return a

# 方法二
def fib_2(n):
	if n == 1 or n == 2:
		return 1
	return fib_2(n - 1) + fib_2(n - 2)

# 输出指定个数的斐波那契数列
def inputfib(n):
	if n == 1:
		return [1]
	if n == 2:
		return [1, 1]
	fibs = [1, 1]
	for i in range(2, n):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs

print(inputfib(10))