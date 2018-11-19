#!/usr/bin/python
# coding:utf-8

"""
列表生成式
List Comprehensions,是Python内置的非常简单且强大的可以用来创建list的生成式
list [1,2,3,4,5,6,7,8,9,10] 可以用 list(range(1, 11))
"""
# list [1,2,3,4,5,6,7,8,9,10]
print(list(range(1, 11)))

# [1*1, 2*2, 3*3, ..., 10*10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 列表生成式则可以用一行语句代替循环生成上面的list
L = [x*x for x in range(1, 11)]
print(L)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L = [x*x for x in range(1, 11) if x % 2 == 0]
print(L)
# 还可以使用两层循环，可以生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 运用列表生成式，可以写出非常简洁的代码，列出当前目录下的所有文件和目录名

# 导入os模块，模块的概念后面讲到
import os
# os.listdir可以列出文件和目录
L = [d for d in os.listdir('.')]
print(L)

# for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
    print(k, '=', v)

# 列表生成式可以使用两个变量来生成list
L1 = [k + '=' + v for k, v in d.items()]
print(L1)

# 最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
# list中所有的字符串首字母大写，其余小写
print([s.capitalize() for s in L])

# 修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L = ['Hello', 'World', 18, 'IBM', 'Apple', 20]
print([s.lower() for s in L if isinstance(s, str)])