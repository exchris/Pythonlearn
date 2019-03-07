#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# Numpy数组属性

import numpy as np

# ndarry.ndim用于返回数组的维数，等于秩
a = np.arange(24)
print(a)
print(a.ndim)  # a现只有一个维度

# 现在调整其大小
b = a.reshape(2, 4, 3)  # b现在用于三个维度
print(b)
print(b.ndim)

# ndarray.shape表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即ndim属性(秩)。
# 比如一个二维数组，其维度表示行数和列数
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

# 调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)

# reshape函数来调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)

# ndarray.itemsize以字节的形式返回数组种每一个元素的大小
# 例如，一个元素类型为 float64 的数组 itemsiz 属性值为 8(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节），又如，一个元素类型为 complex32 的数组 item 属性为 4（32/8）。

# 数组的dtype为int8(一个字节)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)

# ndarray.flags
# ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性：

x = np.array([1, 2, 3, 4, 5])
print(x.flags)
