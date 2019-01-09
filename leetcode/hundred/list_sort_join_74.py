#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 列表排序及连接
# 排序可使用sort()方法，连接可以使用+号或extend()方法

if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    a.sort()  # 对列表a进行排序
    print(a)

    # 连接列表a与b
    print(a + b)

    # 连接列表a与b
    a.extend(b)
    print(a)
