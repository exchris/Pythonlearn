# -*- coding:UTF-8 -*-

# 兔子生兔子算法

a1 = 1
b2 = 1
for i in range(1, 21):
	print("%12ld %121d" %(a1, b2))
	if (i % 3) == 0 :
		print(" ")
	a1 = a1 + b2
	b2 = a1 + b2
	