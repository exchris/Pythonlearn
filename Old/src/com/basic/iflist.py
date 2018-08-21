# -*- coding:UTF-8 -*-
# [1*1,2*2,...10*10]
L = [x*x for x in list(range(1,11))]
print(L)

#  我们只想要偶数的平方,不改动range()的情况下,可以加if来筛选

L2 = [x*x for x in list(range(1,11)) if x%2 == 0]
print(L2)

'''
编写一个函数,它接受一个list,然后把list中的所有字符串变成大写后返回,
非字符串元素将被忽略

提示:
1.isinstance(x,str)可以判断变量x是否是字符串;
2.字符串的upper()方法可以返回大写的字母 
'''

def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]

print(toUppers(['Hello','World',101]))

Lmn = [m+n for m in 'ABC' for n in '123']
print(Lmn)

Lmn1 = []
for m in 'ABC':
	for n in '123':
		Lmn1.append(m+n)


print(Lmn1)

# 利用3层循环的列表生成式,找出对称的3位数
# 例如,121是对称数,因为从右到左倒过来还是121
Ldc = []
for i in list(range(1,10)):
	for j in list(range(0,10)):
		for k in list(range(0, 10)):
			if i == k :
				Ldc.append(100*i+10*j+k)




print(Ldc)
print([100*i+10*j+k*1 for i in list(range(1,10)) for j in list(range(0,10)) for k in list(range(0,10)) if i == k])

print([100*i+10*j+i for i in list(range(1,10)) for j in list(range(0,10))])












