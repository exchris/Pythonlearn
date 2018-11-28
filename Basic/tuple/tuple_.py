#!/usr/bin/python
# -*- coding:utf-8 -*-
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 创建空元祖
tup1 = ()

# 元祖中只包含一个元素时,需要在元素后面添加逗号
tup1 = (50,)

# 访问元祖
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]:", tup1[0], ",tup2[1:5]", tup2[1:5])

# 修改元祖
# 元祖中的元素是不允许修改的，但我们可以对元祖进行连接组合
tup3 = tup1 + tup2
print(tup3)

# 删除元祖
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000)

# print(tup)
# del tup
# print("After deleting tup : ")
# print(tup)

# 元祖运算符
'''
|__python表达式__|__结果__|__描述__|
|-----|------|------|
|len((1,2,3))|3|计算元素个数|
|(1,2,3)+(4,5,6)|(1,2,3,4,5,6)|连接|
|('Hi!',)*4|('Hi!','Hi!','Hi!','Hi!')|复制|
|3 in (1,2,3)|True|元素是否存在|
|for x in(1,2,3):print(x)|1 2 3 |迭代|
'''

# 将列表转换为元祖
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)