#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@description 函数参数的类型决定了它的作用范围,
函数可以修改容器类的数据但不能修改普通变量
@author dev.erxuan@gmail.com
@file function.py
@software PyCharm
@date 2020/4/19 10:02
"""


def change_list(param):
    param.append(4)
    param.append(5)
    param.append(6)


def change_int(param):
    param = 10


if __name__ == "__main__":
    a, b = [1, 2, 3], 0
    print('列表原来为:{}'.format(a))
    change_list(a)
    print('列表被修改为:{}'.format(a))

    print('变量原来为:{}'.format(b))
    change_int(b)
    print('变量现在为:{}'.format(b))
    pass
