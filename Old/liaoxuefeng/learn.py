# -*- coding:utf-8 -*-
def normalize(name):
	# 返回name的首字母大写
	return name.capitalize()

# 测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# ['Adam', 'Lisa', 'Bart']