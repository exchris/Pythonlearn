# -*- coding:utf-8 -*-
# 任意三个整数,安装从小到大的顺序输出

l = []
for i in range(3):
	x = int(input('integer:\n'))
	l.append(x)

l.sort()
print(l)