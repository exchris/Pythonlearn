# -*- coding:UTF-8 -*-
# 九九乘法表

# 完整格式输出九九乘法表
for i in range(1, 10):
	for j in range(1, 10):
		print("%d*%d=%2d" %(i, j, i*j), end = " ")
	print(" ")

# 左上三角格式输出九九乘法表
for i in range(1, 10):
	for j in range(i, 10):
		print("%d*%d=%2d" %(i, j, i*j), end = " ")
	print(" ")

# 右上三角格式输出九九乘法表
for i in range(1, 10):
	for k in range(1, i):
		print( end = "   ")
	for j in range(i, 10):
		print("%d * %d = %2d" %(i,j,i*j),end = " ")
	print(" ")

# 左下三角
for x in range(1, 10):
	for y in range(1, x + 1) :
		print("%d * %d = %2d" %(x, y, x*y), end = "  ")
	print(" ")

# 右下三角
for i in range(1, 10):
	for k in range(1, 10 - i):
		print(end= "   ")
	for j in range(1, i + 1):
		product = i * j
		print("%d*%d=%2d" %(i, j, product), end = " ")
	print(" ")