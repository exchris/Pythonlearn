#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Python内置的一种数据类型是列表:list。
list是一种有序的集合，可以随时添加和删除其中的元素
"""

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print("classmates of length is %d" %len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print("classmates[0] : ", classmates[0])
print("classmates[1] : ", classmates[1])
print("classmates[2] : ", classmates[2])
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，
# 记得最后一个元素的索引时len(list) - 1

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
# 将"Adam"追加到classmates列表中
classmates.append("Adam")
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的未知
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
# 要删除指定位置的元素，用pop(i)方法,其中i是索引位置
print("删除的元素为:", classmates.pop())
print(classmates)